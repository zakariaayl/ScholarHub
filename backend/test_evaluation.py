from app.services.indexer import TFIDFIndexer
from app.services.search import TFIDFSearcher
from app.services.evaluator import SearchEvaluator, TestQueries, evaluate_search_system
from app.services.extractor import DocumentExtractor
from config import Config

def main():
    print("="*60)
    print(" ÉVALUATION DU SYSTÈME DE RECHERCHE")
    print("="*60)
    
    # Étape 1 : Charger ou construire l'index
    print("\n Chargement de l'index...")
    indexer = TFIDFIndexer(language=Config.LANGUAGE, use_stemming=Config.USE_STEMMING)
    
    try:
        # Essayer de charger l'index existant
        indexer.load_from_json('uploads/data/inverted_index.json')
        print(" Index chargé depuis le fichier JSON")
    except FileNotFoundError:
        print(" Index non trouvé, construction d'un nouvel index...")
        documents = DocumentExtractor.process_folder(Config.UPLOAD_FOLDER)
        indexer.build_index(documents)
        indexer.save_to_json('uploads/data/inverted_index.json')
    
    # Étape 2 : Créer le moteur de recherche
    print("\n Initialisation du moteur de recherche...")
    searcher = TFIDFSearcher(indexer)
    
    # Étape 3 : Exécuter les tests d'évaluation
    print("\n Exécution des tests d'évaluation...")
    evaluator = evaluate_search_system(searcher, TestQueries.get_queries())
    
    # Étape 4 : Afficher le résumé
    evaluator.print_evaluation_summary()
    
    # Étape 5 : Générer le rapport JSON
    report = evaluator.generate_evaluation_report('uploads/data/evaluation_report.json')
    
    # Étape 6 : Afficher des exemples pour le rapport
    print("\n" + "="*60)
    print(" EXEMPLES POUR LE RAPPORT TECHNIQUE")
    print("="*60)
    
    for i, eval_result in enumerate(evaluator.evaluation_results[:2], 1):
        print(f"\n Requête {i}: \"{eval_result['query']}\"")
        print("-" * 60)
        
        metrics = eval_result['metrics']
        
        # Matrice de confusion
        print("\nMatrice de confusion:")
        print("                 Pertinent    Non-Pertinent")
        print(f"Retourné           {metrics['tp']:>3}          {metrics['fp']:>3}")
        print(f"Non Retourné       {metrics['fn']:>3}          N/A")
        
        # Métriques
        print(f"\nMétriques:")
        print(f"  Précision = {metrics['tp']}/({metrics['tp']}+{metrics['fp']}) = {metrics['precision']:.4f} ({metrics['precision']:.1%})")
        print(f"  Rappel    = {metrics['tp']}/({metrics['tp']}+{metrics['fn']}) = {metrics['recall']:.4f} ({metrics['recall']:.1%})")
        print(f"  F1-Score  = 2 × ({metrics['precision']:.4f} × {metrics['recall']:.4f}) / ({metrics['precision']:.4f} + {metrics['recall']:.4f}) = {metrics['f1_score']:.4f}")
    
    print("\n" + "="*60)
    print(" ÉVALUATION TERMINÉE AVEC SUCCÈS")
    print("="*60)
    print(f"\n Rapport complet sauvegardé : uploads/data/evaluation_report.json")
    print(" Vous pouvez maintenant utiliser ces résultats dans votre rapport technique")

if __name__ == '__main__':
    main()