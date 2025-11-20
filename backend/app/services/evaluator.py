from typing import List, Dict, Set
import json
from datetime import datetime

class SearchEvaluator:
    """Évaluateur de performances pour le système de recherche"""
    
    def __init__(self):
        self.evaluation_results = []
    
    def calculate_metrics(self, 
                         retrieved_docs: List[int], 
                         relevant_docs: List[int]) -> Dict:
        """
        Calcule les métriques de performance
        
        Args:
            retrieved_docs: Liste des IDs de documents retournés par la recherche
            relevant_docs: Liste des IDs de documents réellement pertinents
        
        Returns:
            Dict avec les métriques: TP, FP, FN, TN, Precision, Recall, F1-Score
        """
        retrieved_set = set(retrieved_docs)
        relevant_set = set(relevant_docs)
        
        # Vrais Positifs : documents pertinents ET retournés
        tp = len(retrieved_set & relevant_set)
        
        # Faux Positifs : documents retournés mais NON pertinents
        fp = len(retrieved_set - relevant_set)
        
        # Faux Négatifs : documents pertinents mais NON retournés
        fn = len(relevant_set - retrieved_set)
        
        # Vrais Négatifs : documents ni pertinents ni retournés
        # (difficile à calculer sans connaître le nombre total de documents)
        # On suppose qu'on a un corpus de N documents
        # TN = N - TP - FP - FN (calculé plus tard si nécessaire)
        
        # Précision : proportion de documents retournés qui sont pertinents
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        
        # Rappel : proportion de documents pertinents qui ont été retournés
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        
        # F1-Score : moyenne harmonique de Précision et Rappel
        f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        return {
            'tp': tp,          # Vrais Positifs
            'fp': fp,          # Faux Positifs
            'fn': fn,          # Faux Négatifs
            'precision': round(precision, 4),
            'recall': round(recall, 4),
            'f1_score': round(f1_score, 4),
            'num_retrieved': len(retrieved_docs),
            'num_relevant': len(relevant_docs)
        }
    
    def evaluate_query(self, 
                      query: str,
                      retrieved_results: List[Dict],
                      relevant_doc_ids: List[int]) -> Dict:
        """
        Évalue une requête spécifique
        
        Args:
            query: La requête testée
            retrieved_results: Résultats retournés par le moteur (liste de dicts avec 'doc_id')
            relevant_doc_ids: Liste des IDs de documents pertinents attendus
        
        Returns:
            Dict avec la requête, les résultats et les métriques
        """
        # Extraire les IDs des documents retournés
        retrieved_doc_ids = [result['doc_id'] for result in retrieved_results]
        
        # Calculer les métriques
        metrics = self.calculate_metrics(retrieved_doc_ids, relevant_doc_ids)
        
        # Construire le résultat complet
        evaluation = {
            'query': query,
            'retrieved_doc_ids': retrieved_doc_ids,
            'relevant_doc_ids': relevant_doc_ids,
            'metrics': metrics,
            'timestamp': datetime.now().isoformat()
        }
        
        # Stocker pour analyse future
        self.evaluation_results.append(evaluation)
        
        return evaluation
    
    def create_confusion_matrix(self, tp: int, fp: int, fn: int, tn: int = 0) -> Dict:
        """
        Crée une matrice de confusion
        
        Returns:
            Dict représentant la matrice de confusion
        """
        return {
            'matrix': [
                ['Pertinent', 'Non Pertinent'],
                [f'Retourné: {tp}', f'Retourné: {fp}'],
                [f'Non Retourné: {fn}', f'Non Retourné: {tn}']
            ],
            'tp': tp,
            'fp': fp,
            'fn': fn,
            'tn': tn
        }
    
    def get_average_metrics(self) -> Dict:
        """
        Calcule les métriques moyennes sur toutes les requêtes évaluées
        
        Returns:
            Dict avec les moyennes de Precision, Recall, F1-Score
        """
        if not self.evaluation_results:
            return {
                'avg_precision': 0.0,
                'avg_recall': 0.0,
                'avg_f1_score': 0.0,
                'num_queries': 0
            }
        
        total_precision = sum(e['metrics']['precision'] for e in self.evaluation_results)
        total_recall = sum(e['metrics']['recall'] for e in self.evaluation_results)
        total_f1 = sum(e['metrics']['f1_score'] for e in self.evaluation_results)
        num_queries = len(self.evaluation_results)
        
        return {
            'avg_precision': round(total_precision / num_queries, 4),
            'avg_recall': round(total_recall / num_queries, 4),
            'avg_f1_score': round(total_f1 / num_queries, 4),
            'num_queries': num_queries
        }
    
    def generate_evaluation_report(self, filepath: str = 'evaluation_report.json'):
        """
        Génère un rapport d'évaluation complet en JSON
        
        Args:
            filepath: Chemin où sauvegarder le rapport
        """
        report = {
            'summary': self.get_average_metrics(),
            'queries': self.evaluation_results,
            'generated_at': datetime.now().isoformat()
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f" Rapport d'évaluation sauvegardé : {filepath}")
        return report
    
    def print_evaluation_summary(self):
        """Affiche un résumé des évaluations dans la console"""
        if not self.evaluation_results:
            print("Aucune évaluation effectuée.")
            return
        
        print("\n" + "="*60)
        print(" RÉSUMÉ DE L'ÉVALUATION")
        print("="*60)
        
        for i, eval_result in enumerate(self.evaluation_results, 1):
            print(f"\n Requête {i}: \"{eval_result['query']}\"")
            print("-" * 60)
            
            metrics = eval_result['metrics']
            print(f"Documents retournés : {metrics['num_retrieved']}")
            print(f"Documents pertinents attendus : {metrics['num_relevant']}")
            print(f"Vrais Positifs (TP) : {metrics['tp']}")
            print(f"Faux Positifs (FP) : {metrics['fp']}")
            print(f"Faux Négatifs (FN) : {metrics['fn']}")
            print(f"\n Métriques:")
            print(f"  Précision  : {metrics['precision']:.2%}")
            print(f"  Rappel     : {metrics['recall']:.2%}")
            print(f"  F1-Score   : {metrics['f1_score']:.4f}")
        
        print("\n" + "="*60)
        print(" MOYENNES GLOBALES")
        print("="*60)
        avg = self.get_average_metrics()
        print(f"Précision moyenne  : {avg['avg_precision']:.2%}")
        print(f"Rappel moyen       : {avg['avg_recall']:.2%}")
        print(f"F1-Score moyen     : {avg['avg_f1_score']:.4f}")
        print(f"Nombre de requêtes : {avg['num_queries']}")
        print("="*60 + "\n")


class TestQueries:
    """Classe contenant les requêtes de test et leurs documents pertinents attendus"""
    
    # Mapping des noms de fichiers aux IDs de documents
    # Basé sur votre index : 0=daad_germany, 1=erasmus, 2=fulbright, 3&4=eiffel
    
    QUERIES = [
        {
            'query': 'intelligence artificielle France',
            'relevant_docs': [3, 4],  # Documents Eiffel (contiennent IA et France)
            'description': 'Recherche bourses IA en France'
        },
        {
            'query': 'master data science Europe',
            'relevant_docs': [1, 3, 4],  # Erasmus (Data Science Europe) + Eiffel (Data Science France/Europe)
            'description': 'Recherche master data science en Europe'
        },
        {
            'query': 'bourse doctorat',
            'relevant_docs': [2, 3, 4],  # Fulbright + Eiffel (tous acceptent doctorat)
            'description': 'Recherche bourses pour doctorat'
        },
        {
            'query': 'Allemagne ingénierie',
            'relevant_docs': [0],  # DAAD Allemagne (ingénierie)
            'description': 'Recherche études ingénierie en Allemagne'
        },
        {
            'query': 'États-Unis programme Fulbright',
            'relevant_docs': [2],  # Fulbright USA
            'description': 'Recherche programme Fulbright aux USA'
        }
    ]
    
    @classmethod
    def get_queries(cls) -> List[Dict]:
        """Retourne la liste des requêtes de test"""
        return cls.QUERIES
    
    @classmethod
    def get_query(cls, index: int) -> Dict:
        """Retourne une requête spécifique par son index"""
        return cls.QUERIES[index] if 0 <= index < len(cls.QUERIES) else None


# Fonction utilitaire pour faciliter l'évaluation
def evaluate_search_system(searcher, test_queries: List[Dict] = None) -> SearchEvaluator:
    """
    Fonction pratique pour évaluer le système de recherche
    
    Args:
        searcher: Instance de TFIDFSearcher
        test_queries: Liste de dicts avec 'query' et 'relevant_docs'
    
    Returns:
        SearchEvaluator avec tous les résultats
    """
    evaluator = SearchEvaluator()
    
    if test_queries is None:
        test_queries = TestQueries.get_queries()
    
    print("\n DÉBUT DE L'ÉVALUATION DU SYSTÈME")
    print("="*60)
    
    for i, test in enumerate(test_queries, 1):
        print(f"\n[{i}/{len(test_queries)}] Test de: \"{test['query']}\"")
        
        # Effectuer la recherche
        results = searcher.search(test['query'], top_k=10)
        
        # Convertir les résultats en format dict si nécessaire
        results_dict = [r.to_dict() if hasattr(r, 'to_dict') else r for r in results]
        
        # Évaluer
        evaluation = evaluator.evaluate_query(
            query=test['query'],
            retrieved_results=results_dict,
            relevant_doc_ids=test['relevant_docs']
        )
        
        # Afficher résumé rapide
        metrics = evaluation['metrics']
        print(f"  ✓ Précision: {metrics['precision']:.2%}, Rappel: {metrics['recall']:.2%}, F1: {metrics['f1_score']:.4f}")
    
    print("\n" + "="*60)
    print(" ÉVALUATION TERMINÉE")
    
    return evaluator