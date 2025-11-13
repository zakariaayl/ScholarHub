import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.extractor import extract_text_from_pdf
from app.services.indexer import index_scholarship

upload_bp = Blueprint("upload_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Extraction texte
    text = extract_text_from_pdf(file_path)

    # Exemple simple de métadonnées (à adapter)
    data = {
        "title": filename,
        "domain": request.form.get("domain", "Inconnu"),
        "country": request.form.get("country", "Non spécifié"),
        "level": request.form.get("level", "Master"),
        "deadline": request.form.get("deadline", "N/A"),
        "description": text[:2000],  # limiter longueur
    }

    index_scholarship(data)
    return jsonify({"message": "Scholarship indexed successfully"}), 201
