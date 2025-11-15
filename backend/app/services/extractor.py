import PyPDF2
import os
from typing import List, Dict
import json

class DocumentExtractor:
    """Extrait le contenu des documents"""
    
    @staticmethod
    def extract_from_pdf(filepath: str) -> str:
        """Extrait le texte d'un PDF"""
        try:
            with open(filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            print(f"Erreur lecture PDF {filepath}: {e}")
            return ""
    
    @staticmethod
    def extract_from_txt(filepath: str) -> str:
        """Lit un fichier texte"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Erreur lecture TXT {filepath}: {e}")
            return ""
    
    @staticmethod
    def extract_from_json(filepath: str) -> Dict:
        """Lit un fichier JSON avec métadonnées"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Concaténer tous les champs textuels
                content = " ".join([
                    str(data.get('titre', '')),
                    str(data.get('description', '')),
                    str(data.get('domaine', '')),
                    str(data.get('pays', ''))
                ])
                return {
                    'content': content,
                    'metadata': data
                }
        except Exception as e:
            print(f"Erreur lecture JSON {filepath}: {e}")
            return {'content': '', 'metadata': {}}
    
    @staticmethod
    def process_folder(folder_path: str) -> List[Dict]:
        """Traite tous les documents d'un dossier"""
        documents = []
        
        if not os.path.exists(folder_path):
            print(f"Le dossier {folder_path} n'existe pas")
            return documents
        
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            
            # Ignorer les sous-dossiers
            if not os.path.isfile(filepath):
                continue
            
            content = ""
            metadata = {}
            
            # Extraction selon le type de fichier
            if filename.endswith('.pdf'):
                content = DocumentExtractor.extract_from_pdf(filepath)
            elif filename.endswith('.txt'):
                content = DocumentExtractor.extract_from_txt(filepath)
            elif filename.endswith('.json'):
                result = DocumentExtractor.extract_from_json(filepath)
                content = result['content']
                metadata = result['metadata']
            else:
                print(f"Format non supporté: {filename}")
                continue
            
            if content:
                documents.append({
                    'filename': filename,
                    'content': content,
                    'metadata': metadata
                })
        
        print(f" {len(documents)} documents extraits")
        return documents