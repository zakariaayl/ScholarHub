from flask import Blueprint, request, jsonify
from app.services.extractor import DocumentExtractor
from app.services.indexer import TFIDFIndexer,SemanticIndexer
from config import Config
import os

upload_sem = Blueprint('uploadSemantic', __name__)


indexer = SemanticIndexer(language=Config.LANGUAGE, use_stemming=Config.USE_STEMMING)
print("indexer is :", indexer)


@upload_sem.route('/index-Semantic', methods=['POST'])
def index_documents():
    try:
        # Extraire les documents
        documents = DocumentExtractor.process_folder(Config.UPLOAD_FOLDER)
        
        if not documents:
            return jsonify({
                'status': 'error',
                'message': 'Aucun document trouvé'
            }), 404
        
        # Construire l'index
        indexer.build_index(documents)
        
        # Sauvegarder dans MongoDB ET JSON (pour le rapport)
        indexer.save_to_mongodb()  # Pour l'application
        indexer.save_to_json()     # Pour le rapport (capture d'écran)
        
        stats = indexer.get_index_stats()
        
        return jsonify({
            'status': 'success',
            'message': f'{len(documents)} documents indexés',
            'stats': stats
        })
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@upload_sem.route('/index-semantic/stats', methods=['GET'])
def get_index_stats():
    """Retourne les statistiques de l'index"""
    if indexer.num_docs == 0:
        return jsonify({
            'status': 'error',
            'message': 'Index non construit. Appelez /index d\'abord'
        }), 400
    
    stats = indexer.get_index_stats()
    return jsonify(stats)