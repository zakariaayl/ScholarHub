import os

class Config:
    # Chemins
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    
    # MongoDB Atlas (Cloud)
    # REMPLACEZ par votre propre connection string
    # MONGO_URI = 'mongodb+srv://searchhub.vkha55v.mongodb.net/" --apiVersion 1 --username Tahalli'
    MONGO_URI= 'mongodb+srv://houcine_db_user:test1234@HoucineCluster.4ii9bex.mongodb.net/?retryWrites=true&w=majority&appName=HoucineCluster'
    MONGO_DB = 'MyTestDB'
    
    # Alternative : MongoDB Local (commenté)
    # MONGO_URI = 'mongodb://localhost:27017/'
    # MONGO_DB = 'sri_bourses'
    
    # Paramètres d'indexation
    USE_STEMMING = True
    USE_LEMMATIZATION = True
    LANGUAGE = 'french'  # ou 'english'
    
    # Paramètres de recherche
    TOP_K_RESULTS = 10
    
    # # Sécurité (optionnel pour production)
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'