from flask import Blueprint, request, jsonify
from app import es
from app.services.recommender import get_similar_scholarships

search_bp = Blueprint("search_bp", __name__)

@search_bp.route("/", methods=["GET"])
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title^3", "domain^2", "country", "level", "description"]
            }
        },
        "sort": [{"publication_date": {"order": "desc"}}]
    }

    results = es.search(index="scholarships", body=body)
    hits = [hit["_source"] for hit in results["hits"]["hits"]]

    # Suggestions IA si un résultat existe
    suggestions = []
    if hits:
        first_title = hits[0]["title"]
        suggestions = get_similar_scholarships(first_title)

    return jsonify({
        "results": hits,
        "suggestions": suggestions
    })
