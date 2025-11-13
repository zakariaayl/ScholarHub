from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app import db

def get_similar_scholarships(title, top_n=5):
    # Charger toutes les bourses
    scholarships = list(db.scholarships.find())
    if not scholarships:
        return []

    docs = [s.get("description", "") for s in scholarships]
    titles = [s.get("title", "") for s in scholarships]

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(docs)

    # Trouver l’index du document cible
    try:
        idx = titles.index(title)
    except ValueError:
        return []

    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]

    return [scholarships[i] for i in similar_indices]
