from datetime import datetime
from typing import List, Dict, Optional

class Document:
    """Modèle pour un document"""
    def __init__(self, doc_id: int, filename: str, content: str, metadata: Optional[Dict] = None):
        self.doc_id = doc_id
        self.filename = filename
        self.content = content
        self.metadata = metadata or {}
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'filename': self.filename,
            'content': self.content,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat()
        }

class SearchResult:
    """Modèle pour un résultat de recherche"""
    def __init__(self, doc_id: int, filename: str, score: float, preview: str, metadata: Dict = None):
        self.doc_id = doc_id
        self.filename = filename
        self.score = score
        self.preview = preview
        self.metadata = metadata or {}
    
    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'filename': self.filename,
            'score': round(self.score, 4),
            'preview': self.preview,
            'metadata': self.metadata
        }
class SearchResultSemantic:
    def __init__(self, doc_id, filename, score, preview):
        self.doc_id = doc_id
        self.filename = filename
        self.score = score
        self.preview = preview

    def to_dict(self):
        # Déboguer pour vérifier le type
        if not isinstance(self, SearchResultSemantic):
            raise TypeError(f"Expected SearchResult, got {type(self)}")
        return {
            'doc_id': self.doc_id,
            'filename': self.filename,
            'score': float(self.score),
            'preview': self.preview
        }


class InvertedIndex:
    """Modèle pour l'inverted index"""
    def __init__(self):
        self.index = {}  # {term: [(doc_id, tf), ...]}
        self.documents = {}  # {doc_id: Document}
        self.idf = {}  # {term: idf_value}
        self.doc_count = 0