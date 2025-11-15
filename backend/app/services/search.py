from typing import List, Dict
from collections import defaultdict
from ..models import SearchResult

class TFIDFSearcher:
    """Moteur de recherche TF-IDF"""
    
    def __init__(self, indexer):
        self.indexer = indexer
    
    def search(self, query: str, top_k: int = 10) -> List[SearchResult]:
        """
        Recherche les documents pertinents pour une requête
        Retourne une liste de SearchResult triée par score décroissant
        """
        # Prétraiter la requête
        query_tokens = self.indexer.preprocessor.preprocess(query)
        
        if not query_tokens:
            return []
        
        # Calculer les scores TF-IDF pour chaque document
        scores = defaultdict(float)
        
        for term in query_tokens:
            if term in self.indexer.inverted_index:
                idf = self.indexer.idf[term]
                
                # Pour chaque document contenant le terme
                for doc_id, tf in self.indexer.inverted_index[term]:
                    # Score TF-IDF = TF × IDF
                    tfidf_score = tf * idf
                    scores[doc_id] += tfidf_score
        
        # Trier par score décroissant
        ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Construire les résultats
        results = []
        for doc_id, score in ranked_docs[:top_k]:
            doc = self.indexer.documents[doc_id]
            
            # Créer un aperçu du contenu
            preview = doc['content'][:300] + '...' if len(doc['content']) > 300 else doc['content']
            
            result = SearchResult(
                doc_id=doc_id,
                filename=doc['filename'],
                score=score,
                preview=preview,
                metadata=doc.get('metadata', {})
            )
            results.append(result)
        
        return results
    
    def search_with_filters(self, query: str, filters: Dict = None, top_k: int = 10) -> List[SearchResult]:
        """
        Recherche avec filtres sur les métadonnées
        filters = {'pays': 'France', 'domaine': 'IA'}
        """
        # Recherche initiale
        results = self.search(query, top_k=100)  # Récupérer plus pour filtrer
        
        if not filters:
            return results[:top_k]
        
        # Appliquer les filtres
        filtered_results = []
        for result in results:
            match = True
            for key, value in filters.items():
                if result.metadata.get(key) != value:
                    match = False
                    break
            
            if match:
                filtered_results.append(result)
        
        return filtered_results[:top_k]