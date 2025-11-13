from datetime import datetime
from app import db

class Scholarship:
    """
    Modèle représentant une bourse ou un programme universitaire.
    Les données sont stockées dans MongoDB et indexées dans Elasticsearch.
    """

    def __init__(self, title, domain, country, level, deadline, description, source="local"):
        self.title = title
        self.domain = domain
        self.country = country
        self.level = level
        self.deadline = deadline
        self.description = description
        self.source = source          # 'local' (PDF/ajout manuel) ou 'web'
        self.publication_date = datetime.now()

    def to_dict(self):
        """Convertit l’objet en dictionnaire pour MongoDB ou Elasticsearch."""
        return {
            "title": self.title,
            "domain": self.domain,
            "country": self.country,
            "level": self.level,
            "deadline": self.deadline,
            "description": self.description,
            "source": self.source,
            "publication_date": self.publication_date.isoformat(),
        }

    def save(self):
        """Sauvegarde le document dans MongoDB."""
        db.scholarships.insert_one(self.to_dict())

    @staticmethod
    def find_all():
        """Retourne toutes les bourses stockées."""
        return list(db.scholarships.find())

    @staticmethod
    def find_by_title(title):
        """Cherche une bourse par titre."""
        return db.scholarships.find_one({"title": title})

    @staticmethod
    def delete_by_title(title):
        """Supprime une bourse selon son titre."""
        db.scholarships.delete_one({"title": title})
