from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask import jsonify, Response
import json
from ..models import SearchResultSemantic  # Assurez-vous que SearchResult est bien défini dans models.py

class SemanticSearcher:
    """Moteur de recherche sémantique basé sur les embeddings"""
    
    def __init__(self, indexer):
        self.indexer = indexer
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Modèle de transformation
    
    def convert_to_native_types(self, obj):
        """Convertir les objets NumPy (comme float32) en types natifs de Python."""
        if isinstance(obj, np.ndarray):
            return obj.tolist()  # Convertir un array NumPy en liste native
        elif isinstance(obj, np.float32):
            return float(obj)  # Convertir float32 en float
        # Ajouter d'autres types selon les besoins
        return obj

    def search(self, query: str, top_k: int = 10):
        """Recherche les documents pertinents pour une requête"""

        # Prétraiter la requête et obtenir son embedding
        query_embedding = self.model.encode([query])   # SentenceTransformer retourne déjà un tableau 2D
        print(f"query_embedding shape: {query_embedding.shape}")  # Debug

        if query_embedding is None or np.all(np.isnan(query_embedding)):
            return jsonify({'error': 'No results found'}), 400

        # Vérifier la dimension de `query_embedding`
        if len(query_embedding.shape) == 1:
            query_embedding = query_embedding.reshape(1, -1)  # Convertir en 2D si nécessaire
        print(f"query_embedding reshaped to: {query_embedding.shape}")  # Debug

        # Récupérer les embeddings des documents
        document_embeddings = np.array(self.indexer.document_embeddings)  # Convertir en tableau numpy pour la gestion
        print(f"document_embeddings shape before reshape: {document_embeddings.shape}")  # Debug

        # Vérifier et aplatir chaque embedding si nécessaire
        if len(document_embeddings.shape) == 3:
            document_embeddings = document_embeddings.reshape(document_embeddings.shape[0], -1)  # Flatten en 2D
        print(f"document_embeddings reshaped to: {document_embeddings.shape}")  # Debug

        # Calculer les similarités cosinus
        similarities = cosine_similarity(query_embedding, document_embeddings)  # Matrice 2D attendue
        print(f"similarities shape: {similarities.shape}")  # Debug

        # Trier les documents par similarité décroissante
        ranked_docs = sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=True)

        # Construire les résultats
        results = []
        for doc_idx, score in ranked_docs[:top_k]:
            try:
                doc = self.indexer.documents[doc_idx]
            except KeyError:
                continue  # Skip if document is not found

            preview = doc.get('content', '')[:300] + '...' if len(doc.get('content', '')) > 300 else doc.get('content', '')
            result = SearchResultSemantic(doc_id=doc_idx, filename=doc['filename'], score=score, preview=preview)
            results.append(result)

        # Convertir les résultats en format natif (JSON serializable)
        results_json = [self.convert_to_native_types(result.to_dict()) for result in results]

        # Créer un dictionnaire avec les résultats et la requête
        response_data = {
            'query': query,
            'results': results_json
        }

        # Si vous souhaitez manipuler la réponse avant d'utiliser jsonify, assurez-vous que vous retournez un dictionnaire.
        # Pas besoin de 'jsonify' avant cela. 

        # Si vous voulez vraiment utiliser `jsonify`:
        return jsonify(response_data)
