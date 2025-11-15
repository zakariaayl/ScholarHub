from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from config import Config
import sys

class MongoDB:
    """Gestionnaire de connexion MongoDB Atlas"""
    
    def __init__(self):
        self.client = None
        self.db = None
    
    def connect(self):
        """Établir la connexion à MongoDB Atlas"""
        try:
            print(" Connexion à MongoDB Atlas...")
            
            # Créer le client avec timeout
            self.client = MongoClient(
                Config.MONGO_URI,
                serverSelectionTimeoutMS=5000  # Timeout 5 secondes
            )
            
            # Tester la connexion
            self.client.admin.command('ping')
            
            # Sélectionner la base de données
            self.db = self.client[Config.MONGO_DB]
            
            print(f" Connecté à MongoDB Atlas : {Config.MONGO_DB}")
            return self.db
        
        except ServerSelectionTimeoutError:
            print(" Erreur : Impossible de se connecter à MongoDB Atlas")
            print("Vérifiez :")
            print("  1. Votre connexion Internet")
            print("  2. Que votre IP est autorisée dans Network Access")
            print("  3. Que la connection string est correcte")
            return None
        
        except ConnectionFailure:
            print(" Erreur : Échec de connexion à MongoDB")
            print("Vérifiez vos identifiants (username/password)")
            return None
        
        except Exception as e:
            print(f" Erreur connexion MongoDB : {e}")
            return None
    
    def get_collection(self, collection_name):
        """Récupérer une collection"""
        if self.db is None:
            self.connect()
        
        if self.db is None:
            raise Exception("Impossible de se connecter à MongoDB")
        
        return self.db[collection_name]
    
    def test_connection(self):
        """Tester la connexion et afficher les infos"""
        try:
            db = self.connect()
            if db is None:
                return False
            
            # Afficher les collections existantes
            collections = db.list_collection_names()
            print(f"\n Collections dans '{Config.MONGO_DB}':")
            if collections:
                for col in collections:
                    count = db[col].count_documents({})
                    print(f"  - {col}: {count} documents")
            else:
                print("  (Aucune collection)")
            
            return True
        
        except Exception as e:
            print(f" Test échoué : {e}")
            return False
    
    def drop_database(self):
        """Supprimer la base de données (attention !)"""
        if self.client:
            self.client.drop_database(Config.MONGO_DB)
            print(f" Base de données '{Config.MONGO_DB}' supprimée")
    
    def close(self):
        """Fermer la connexion"""
        if self.client:
            self.client.close()
            print(" Connexion MongoDB fermée")

# Instance globale
mongodb = MongoDB()

# Test de connexion si exécuté directement
if __name__ == '__main__':
    print("=== Test de connexion MongoDB Atlas ===\n")
    if mongodb.test_connection():
        print("\n Connexion réussie !")
    else:
        print("\n Échec de connexion")
        sys.exit(1)