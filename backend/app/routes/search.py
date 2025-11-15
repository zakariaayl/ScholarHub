from flask import Blueprint, request, jsonify
from app.services.search import TFIDFSearcher
from app.routes.upload import indexer  # Importer l'indexeur global

search_bp = Blueprint('search', __name__)

# Instance du moteur de recherche
searcher = None

@search_bp.route('/search', methods=['GET'])
def search():
    """
    Endpoint de recherche
    Paramètres:
        - q: requête (obligatoire)
        - top_k: nombre de résultats (optionnel, défaut=10)
        - pays: filtre par pays (optionnel)
        - domaine: filtre par domaine (optionnel)
    """
    global searcher
    
    # Vérifier que l'index est construit
    if indexer.num_docs == 0:
        return jsonify({
            'status': 'error',
            'message': 'Index non construit. Appelez /index d\'abord'
        }), 400
    
    # Initialiser le searcher si nécessaire
    if searcher is None:
        searcher = TFIDFSearcher(indexer)
    
    # Récupérer les paramètres
    query = request.args.get('q', '').strip()
    top_k = int(request.args.get('top_k', 10))
    
    if not query:
        return jsonify({
            'status': 'error',
            'message': 'Paramètre "q" (requête) requis'
        }), 400
    
    # Récupérer les filtres optionnels
    filters = {}
    if request.args.get('pays'):
        filters['pays'] = request.args.get('pays')
    if request.args.get('domaine'):
        filters['domaine'] = request.args.get('domaine')
    
    # Recherche
    if filters:
        results = searcher.search_with_filters(query, filters, top_k)
    else:
        results = searcher.search(query, top_k)
    
    # Convertir en JSON
    results_json = [r.to_dict() for r in results]
    
    return jsonify({
        'query': query,
        'filters': filters,
        'count': len(results_json),
        'results': results_json
    })