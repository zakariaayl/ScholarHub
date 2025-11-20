import math
import string
from collections import defaultdict
from typing import List, Dict, Tuple
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import json

# Télécharger ressources NLTK (à faire une seule fois)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

class TextPreprocessor:
    """Prétraitement du texte"""
    
    def __init__(self, language='french', use_stemming=True):
        self.language = language
        self.use_stemming = use_stemming
        
        # Charger stop words (français + anglais)
        self.stop_words = set(
            stopwords.words('french') 
            # stopwords.words('english')
        )
        
        # Stemmer
        self.stemmer = SnowballStemmer(language) if use_stemming else None
    
    def preprocess(self, text: str) -> List[str]:
        """
        Nettoie et normalise le texte
        1. Minuscules
        2. Suppression ponctuation
        3. Tokenization
        4. Suppression stop words
        5. Stemming (optionnel)
        """
        # Minuscules
        text = text.lower()
        
        # Supprimer ponctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenization
        try:
            tokens = word_tokenize(text, language=self.language)
        except:
            tokens = text.split()
        
        # Filtrer stop words et mots courts
        tokens = [
            word for word in tokens 
            if word not in self.stop_words and len(word) > 2
        ]
        
        # Stemming
        if self.use_stemming and self.stemmer:
            tokens = [self.stemmer.stem(word) for word in tokens]
        
        return tokens


class TFIDFIndexer:
    """Indexeur TF-IDF"""
    
    def __init__(self, language='french', use_stemming=True):
        self.preprocessor = TextPreprocessor(language, use_stemming)
        
        # Structure de l'inverted index
        self.inverted_index = defaultdict(list)  # {terme: [(doc_id, tf), ...]}
        self.documents = {}  # {doc_id: Document}
        self.idf = {}  # {terme: idf_score}
        self.doc_lengths = {}  # {doc_id: nombre_tokens}
        self.num_docs = 0
    
    def calculate_tf(self, tokens: List[str]) -> Dict[str, float]:
        """Calcule Term Frequency pour une liste de tokens"""
        term_freq = defaultdict(int)
        for token in tokens:
            term_freq[token] += 1
        
        # Normaliser par la longueur du document
        num_tokens = len(tokens)
        tf_normalized = {
            term: count / num_tokens 
            for term, count in term_freq.items()
        } if num_tokens > 0 else {}
        
        return tf_normalized
    
    def build_index(self, documents: List[Dict]):
        """
        Construit l'inverted index à partir d'une liste de documents
        documents = [{'filename': ..., 'content': ..., 'metadata': ...}, ...]
        """
        print(" Construction de l'index inversé...")
        
        self.num_docs = len(documents)
        
        # Phase 1 : Construire l'index et calculer TF
        for doc_id, doc in enumerate(documents):
            content = doc['content']
            
            # Prétraiter le texte
            tokens = self.preprocessor.preprocess(content)
            
            # Stocker le document
            self.documents[doc_id] = doc
            self.doc_lengths[doc_id] = len(tokens)
            
            # Calculer TF
            tf_scores = self.calculate_tf(tokens)
            
            # Ajouter à l'inverted index
            for term, tf in tf_scores.items():
                self.inverted_index[term].append((doc_id, tf))
        
        # Phase 2 : Calculer IDF
        self.calculate_idf()
        
        print(f" Index construit : {len(self.inverted_index)} termes uniques")
        print(f" {self.num_docs} documents indexés")
    
    def calculate_idf(self):
        """Calcule Inverse Document Frequency pour tous les termes"""
        for term, postings in self.inverted_index.items():
            df = len(postings)  # Document Frequency
            # IDF = log(N / df)
            self.idf[term] = math.log(self.num_docs / df) if df > 0 else 0
    
    def get_index_stats(self) -> Dict:
        """Retourne des statistiques sur l'index"""
        return {
            'num_documents': self.num_docs,
            'num_terms': len(self.inverted_index),
            'avg_doc_length': sum(self.doc_lengths.values()) / self.num_docs if self.num_docs > 0 else 0,
            'top_terms': self.get_top_terms(10)
        }
    
    def get_top_terms(self, n=10) -> List[Tuple[str, int]]:
        """Retourne les n termes les plus fréquents"""
        term_counts = {
            term: len(postings) 
            for term, postings in self.inverted_index.items()
        }
        sorted_terms = sorted(term_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_terms[:n]
    
    def save_to_json(self, filepath='uploads/data/inverted_index.json'):
        """Sauvegarde l'index en JSON"""
        data = {
            'inverted_index': {
                term: postings 
                for term, postings in self.inverted_index.items()
            },
            'documents': self.documents,
            'idf': self.idf,
            'doc_lengths': self.doc_lengths,
            'num_docs': self.num_docs
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f" Index sauvegardé dans {filepath}")
    
    def load_from_json(self, filepath='uploads/data/inverted_index.json'):
        """Charge l'index depuis JSON"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.inverted_index = defaultdict(list, data['inverted_index'])
        self.documents = {int(k): v for k, v in data['documents'].items()}
        self.idf = data['idf']
        self.doc_lengths = {int(k): v for k, v in data['doc_lengths'].items()}
        self.num_docs = data['num_docs']
        
        print(f" Index chargé depuis {filepath}")


    def save_to_mongodb(self):
     from app.utils.db import mongodb
    
     db = mongodb.connect()
     if db is None:
        print(" Impossible de se connecter à MongoDB")
        return False
    
     try:
        # Collection pour l'inverted index
        index_collection = db['inverted_index']
        index_collection.delete_many({})  # Nettoyer
        
        # Insérer les termes avec leurs postings
        for term, postings in self.inverted_index.items():
            index_collection.insert_one({
                'term': term,
                'postings': postings,
                'idf': self.idf[term],
                'doc_frequency': len(postings)
            })
        
        # Collection pour les documents
        docs_collection = db['documents']
        docs_collection.delete_many({})
        
        for doc_id, doc in self.documents.items():
            docs_collection.insert_one({
                'doc_id': doc_id,
                'filename': doc['filename'],
                'content': doc['content'],
                'metadata': doc.get('metadata', {}),
                'length': self.doc_lengths[doc_id]
            })
        
        # Collection pour les métadonnées de l'index
        meta_collection = db['index_metadata']
        meta_collection.delete_many({})
        meta_collection.insert_one({
            'num_documents': self.num_docs,
            'num_terms': len(self.inverted_index),
            'indexed_at': datetime.now()
        })
        
        print(f" Index sauvegardé dans MongoDB ({len(self.inverted_index)} termes)")
        return True
    
     except Exception as e: 
        print(f" Erreur sauvegarde MongoDB : {e}")
        return False