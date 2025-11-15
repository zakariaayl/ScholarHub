from flask import Flask
from flask_cors import CORS
from app.routes.search import search_bp
from app.routes.upload import upload_bp
from config import Config
import os

# Créer l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Activer CORS
CORS(app)

# Créer le dossier uploads s'il n'existe pas
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Enregistrer les blueprints
app.register_blueprint(search_bp, url_prefix='/api')
app.register_blueprint(upload_bp, url_prefix='/api')

@app.route('/')
def home():
    return {
        'message': 'API SRI - Moteur de recherche de bourses',
        'endpoints': {
            'indexation': '/api/index (POST)',
            'statistiques': '/api/index/stats (GET)',
            'recherche': '/api/search?q=<query> (GET)'
        }
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
