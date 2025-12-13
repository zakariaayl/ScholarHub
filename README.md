# 🎓 Intelligent International Scholarship Search System (SRI)

> **Un système intelligent de recherche de bourses et programmes universitaires internationaux, combinant la robustesse de la recherche lexicale (TF-IDF) et la finesse de la recherche sémantique (BERT).**

<br>

## 🚀 Démarrage Rapide

| Aspect | Recherche Lexicale (TF-IDF) | Recherche Sémantique (BERT) |
|:---|:---|:---|
| **Vitesse** | ⚡⚡⚡ **Très rapide** | ⚡ Modéré |
| **Contexte** | ❌ Non (Mots-clés exacts) | ✅ **Oui** (Sens et Intention) |
| **Précision** | 68% (Correspondance des termes) | 75% |
| **F1-Score (Fusion)** | | **0.90** |

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18.0%2B-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0%2B-13AA52?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 💡 À Propos du Projet

Le processus de recherche de bourses universitaires est souvent fragmenté et chronophage. Ce projet vise à créer une **plateforme centralisée et intelligente** pour résoudre ce problème d'accessibilité.

En combinant deux moteurs de recherche puissants, le système fournit des **résultats précis et contextualisés** même pour des requêtes en langage naturel (e.g., "Je cherche une bourse pour un master en Data Science en France").

### Avantages Clés
* ✅ **Index Centralisé** : Catalogue de 50+ bourses internationales.
* ✅ **Recherche Hybride** : Fusion des résultats TF-IDF et BERT pour une pertinence maximale.
* ✅ **Interface Utilisateur (UI)** : Intuitive, développée avec React, offrant une vue comparative des résultats.
* ✅ **Scalabilité** : Backend performant avec Flask et stockage optimisé via MongoDB Atlas.

---

## ✨ Fonctionnalités Principales

* **🔍 Double Approche de Recherche** : Permet aux utilisateurs de visualiser les forces de la recherche lexicale *vs* sémantique avant la fusion finale.
* **📊 Filtrage Avancé** : Résultats filtrables par Pays, Domaine d'étude et Niveau (Licence, Master, Doctorat).
* **⚙️ API REST Complète** : Facile à intégrer à d'autres applications ou services.
* **📄 Traitement NLP** : Inclut le _Stemming_ français et la suppression des _Stop Words_ via NLTK pour une indexation optimisée.
* **🔄 Indexation Automatique** : Support pour l'ingestion de documents PDF, TXT et JSON.

---

## 🏗️ Architecture du Système

Le projet est divisé en trois composants principaux : **Frontend (React)**, **Backend (Flask)**, et la **Couche de Persistance (MongoDB)**.

### Vue d'ensemble du Flux



### 1. Frontend (React.js)
* Interface utilisateur moderne et réactive.
* Gère les requêtes utilisateur et l'affichage comparatif des résultats.

### 2. Backend (Flask)
* Fournit l'API RESTful.
* Orchestre l'exécution des deux moteurs de recherche.
* Implémente la logique de **Fusion des Résultats** et de classement final.

### 3. Moteurs de Recherche

| Composant | Technologie | Rôle |
|:---|:---|:---|
| **Lexicale** | **TF-IDF (scikit-learn)** | Matching rapide et précis des termes exacts. |
| **Sémantique** | **Sentence-BERT** | Génère des _embeddings_ (vecteurs) pour comprendre le sens des requêtes/documents et utilise la **Similarité Cosinus**. |
| **Stockage** | **MongoDB Atlas** | Stocke les documents indexés et les vecteurs BERT (vector DB). |

---

## 💻 Technologies Utilisées

| Catégorie | Outils Clés |
|:---|:---|
| **Frontend** | `React 18+`, `Axios`, `Tailwind CSS`, `React Router` |
| **Backend** | `Python 3.8+`, `Flask 2.0+`, `Flask-CORS` |
| **Recherche/NLP** | `scikit-learn (TF-IDF)`, `Sentence-BERT`, `NLTK`, `Snowball Stemmer` |
| **Base de Données** | `MongoDB Atlas` |
| **Développement** | `Git`, `Pipenv/venv`, `npm` |

---

## 🚀 Installation et Démarrage

### Prérequis
* `Python 3.8` ou supérieur
* `Node.js 14+` et `npm`
* Compte gratuit `MongoDB Atlas` (pour la base de données)
* `Git`

### Étape 1 : Cloner et Configurer
```bash
git clone [https://github.com/your-username/sri-bourses.git](https://github.com/your-username/sri-bourses.git)
cd sri-bourses
