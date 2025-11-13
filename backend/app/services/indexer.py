from datetime import datetime
from app import es, db

def index_scholarship(data):
    # Sauvegarde MongoDB
    db.scholarships.insert_one(data)

    # Indexation Elasticsearch
    doc = {
        "title": data.get("title", ""),
        "domain": data.get("domain", ""),
        "country": data.get("country", ""),
        "level": data.get("level", ""),
        "deadline": data.get("deadline", ""),
        "description": data.get("description", ""),
        "publication_date": datetime.now().isoformat()
    }

    es.index(index="scholarships", document=doc)
