from flask import Blueprint, request, jsonify
from app.services.semantic_search import SemanticSearcher
from app.routes.uploadSemantic import indexer  # Importer l'indexeur global

search_sem = Blueprint('search_sem', __name__)

# Instance du moteur de recherche
searcher = None



@search_sem.route('/semantic-search', methods=['GET'])
def search():
    global searcher
    
    if indexer.num_docs == 0:
        return jsonify({
            'status': 'error',
            'message': "Index non construit. Appelez /index d'abord"
        }), 400

    if searcher is None:
        searcher = SemanticSearcher(indexer)

    query = request.args.get('q', '').strip()
    top_k = int(request.args.get('top_k', 10))

    if not query:
        return jsonify({
            'status': 'error',
            'message': 'Paramètre "q" requis'
        }), 400

    filters = {}
    if request.args.get('pays'):
        filters['pays'] = request.args.get('pays')
    if request.args.get('domaine'):
        filters['domaine'] = request.args.get('domaine')

    # Appel du moteur de recherche → qui retourne déjà jsonify(...)
    if filters:
        return searcher.search_with_filters(query, filters, top_k)
    else:
        return searcher.search(query, top_k)
