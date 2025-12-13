# 🎓 Système de Recherche d'Information (SRI)
## Bourses et Programmes Universitaires Internationaux

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18.0%2B-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0%2B-13AA52?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Un système intelligent de recherche de bourses et programmes universitaires internationaux combinant deux approches : **recherche lexicale (TF-IDF)** et **recherche sémantique (BERT)**.

---

## 📋 Table des matières

- [À propos](#-à-propos)
- [Caractéristiques](#-caractéristiques)
- [Architecture](#-architecture)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [Moteurs de recherche](#-moteurs-de-recherche)
- [Évaluation](#-évaluation)
- [Structure du projet](#-structure-du-projet)
- [Contribution](#-contribution)
- [License](#-license)

---

## 💡 À propos

Ce projet vise à **résoudre le problème d'accessibilité** aux bourses universitaires internationales. Les étudiants perdent du temps à naviguer entre différents portails et sources d'information dispersées.

Notre solution offre :
- ✅ Un **index centralisé** de 50+ bourses internationales
- ✅ Deux **moteurs de recherche complémentaires**
- ✅ Une **interface utilisateur intuitive**
- ✅ Des **résultats précis et contextualisés**

### 🌍 Bourses supportées

| Pays | Programme | Niveau |
|------|-----------|--------|
| 🇩🇪 Allemagne | DAAD | Master |
| 🇪🇺 Europe | Erasmus Mundus | Master |
| 🇺🇸 États-Unis | Fulbright | Master, Doctorat |
| 🇬🇧 Royaume-Uni | Chevening | Master |
| 🇨🇭 Suisse | Swiss Excellence | Doctorat |
| 🇫🇷 France | Eiffel Excellence | Master, Doctorat |
| 🇧🇪 Belgique | ARES | Master |
| 🇦🇹 Autriche | OeAD | Master, Recherche |
| 🇪🇸 Espagne | Fundación Carolina | Master |
| 🇭🇺 Hongrie | Hungaricum | Tous niveaux |
| *Et 7 autres...* | | |

---

## ✨ Caractéristiques

### 🔍 Double approche de recherche

```
┌─────────────────────────────────────────────────────────┐
│                  REQUÊTE UTILISATEUR                     │
│          "Master Intelligence Artificielle"              │
└────────────────────────┬────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
    ┌──────────────┐             ┌──────────────┐
    │ TF-IDF       │             │ BERT         │
    │ (Lexical)    │             │ (Semantic)   │
    └──────┬───────┘             └──────┬───────┘
           │                            │
           │ Résultats 1-5             │ Résultats 1-5
           │ Précision: 14-50%         │ Précision: 70-95%
           │                            │
           └──────────────┬─────────────┘
                          ▼
            ┌──────────────────────────┐
            │  FUSION DES RÉSULTATS    │
            │  (Meilleurs matchs)      │
            └──────────────────────────┘
```

### 📊 Fonctionnalités principales

- **Recherche en temps réel** : Résultats instantanés
- **Comparaison d'approches** : Voir les deux moteurs côte à côte
- **Filtrage avancé** : Par pays, domaine, niveau d'études
- **Stockage optimisé** : MongoDB pour scalabilité
- **API REST complète** : Intégration facile
- **Indexation automatique** : Support PDF, TXT, JSON
- **Traitement NLP** : Stemming français, suppression stop words

---

## 🏗️ Architecture

### Vue d'ensemble du système

```
┌─────────────────────────────────────────────────────────┐
│                    UTILISATEUR                           │
│                                                          │
│     Saisit une requête : "bourse master France"         │
└─────────────────────┬──────────────────────────────────┘
                      │
                      ▼ HTTP POST
┌─────────────────────────────────────────────────────────┐
│              FRONTEND (React.js)                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │ • Composants UI                                │   │
│  │ • Gestion d'état (Redux/Context)               │   │
│  │ • Requêtes API (Axios)                         │   │
│  │ • Affichage comparatif des résultats          │   │
│  └─────────────────────────────────────────────────┘   │
└──────────────┬──────────────────────────────────────────┘
               │ API /search
               ▼
┌──────────────────────────────────────────────────────────┐
│               BACKEND (Flask)                            │
│  ┌────────────────────────────────────────────────────┐ │
│  │ • API REST Endpoints                             │ │
│  │ • Middleware & CORS                              │ │
│  │ • Validation des requêtes                        │ │
│  └────────────────────────────────────────────────────┘ │
│                    │                                     │
│       ┌────────────┴────────────┐                       │
│       ▼                         ▼                       │
│  ┌──────────────┐         ┌──────────────┐            │
│  │ TF-IDF       │         │ BERT         │            │
│  │ Searcher     │         │ Semantic     │            │
│  │ • Indexing   │         │ Searcher     │            │
│  │ • Ranking    │         │ • Embeddings │            │
│  └────────┬─────┘         └───────┬──────┘            │
│           │                       │                    │
│           └───────────┬───────────┘                    │
│                       ▼                                │
│              ┌───────────────────┐                    │
│              │ Result Fusion     │                    │
│              │ & Ranking         │                    │
│              └────────┬──────────┘                    │
└─────────────────────┬─────────────────────────────────┘
                      │ JSON Response
                      ▼
         ┌─────────────────────────┐
         │  FRONTEND               │
         │  Affiche résultats      │
         │  • TF-IDF Results       │
         │  • BERT Results         │
         │  • Best Matches         │
         └─────────────────────────┘
```

### Flux de données

```
Documents (PDF, TXT) 
         │
         ▼
    ┌─────────────────┐
    │ Extraction &    │
    │ Prétraitement   │
    │ • Tokenization  │
    │ • Stemming      │
    │ • Stop words    │
    └────────┬────────┘
             │
    ┌────────┴────────────┐
    ▼                     ▼
┌─────────────┐     ┌──────────────┐
│ TF-IDF      │     │ BERT Model   │
│ Indexing    │     │ Embeddings   │
│             │     │              │
│ Inverted    │     │ Vector DB    │
│ Index       │     │ (Sentence    │
│             │     │ embeddings)  │
└────────┬────┘     └──────┬───────┘
         │                  │
         └────────┬─────────┘
                  ▼
          MongoDB Atlas
```

---

## 💻 Technologies

### Frontend
- **React 18.0+** - Framework UI
- **Axios** - Client HTTP
- **Tailwind CSS** - Styling
- **React Router** - Navigation

### Backend
- **Python 3.8+** - Langage
- **Flask 2.0+** - Framework web
- **Flask-CORS** - Gestion CORS
- **MongoDB Atlas** - Base de données

### Moteurs de recherche
| Composant | Technologie | Description |
|-----------|-------------|-------------|
| **Recherche Lexicale** | TF-IDF + scikit-learn | Matching rapide basé sur les termes |
| **Recherche Sémantique** | Sentence-BERT | Compréhension contextuelle |
| **Traitement NLP** | NLTK + Snowball Stemmer | Traitement français optimisé |
| **Indexation** | Inverted Index | Index inversé pour performance |

---

## 🚀 Installation

### Prérequis

```bash
✓ Python 3.8 ou supérieur
✓ Node.js 14+ et npm
✓ MongoDB Atlas (compte gratuit disponible)
✓ Git
```

### Étape 1 : Cloner le repository

```bash
git clone https://github.com/your-username/sri-bourses.git
cd sri-bourses
```

### Étape 2 : Setup Backend

#### Créer l'environnement virtuel
```bash
python -m venv venv

# Activation
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### Installer les dépendances
```bash
pip install -r requirements.txt
```

### Étape 3 : Setup Frontend

```bash
cd frontend
npm install
```

### Étape 4 : Lancer l'application

**Terminal 1 - Backend:**
```bash
python run.py
```

**Terminal 2 - Frontend:**
```bash
npm start
```

---
### Configuration MongoDB

1. Créer un compte sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Créer un cluster gratuit
3. Ajouter une IP whitelist
4. Générer les credentials
5. Remplacer `MONGODB_URI` dans `.env`

---

## 📱 Utilisation

### 1. Interface de recherche

```
┌──────────────────────────────────────┐
│  🔍 Rechercher une Bourse            │
├──────────────────────────────────────┤
│                                      │
│  Entrez votre requête:               │
│  [Saisir votre requête...]           │
│  [🔍 Rechercher]                     │
│                                      │
│  Exemples:                           │
│  • "Master Intelligence Artificielle"│
│  • "Bourse doctorat France"         │
│  • "Ingénierie Allemagne DAAD"      │
│                                      │
└──────────────────────────────────────┘
```

### 2. Résultats

L'application affiche les résultats de deux moteurs:

#### 🔤 Résultats TF-IDF (Lexical)
- Basé sur la correspondance des termes
- Rapide et précis pour des requêtes spécifiques
- Idéal pour: noms de programmes, pays, mots clés

#### 🧠 Résultats BERT (Sémantique)
- Comprend le sens et le contexte
- Gère mieux les variations lexicales
- Idéal pour: descriptions, phrases naturelles

#### 🏆 Meilleurs résultats (Fusion)
- Combine les deux approches
- Classement automatique par pertinence

### 3. Exemples de requêtes

```
✓ "bourse master France"
✓ "Fulbright doctorat États-Unis"
✓ "Erasmus master data science Europe"
✓ "Chevening leadership Royaume-Uni"
✓ "intelligence artificielle Eiffel"
```

---

## 🔍 Moteurs de recherche

### TF-IDF (Term Frequency - Inverse Document Frequency)

**Approche:** Lexicale - Matching de termes

**Formule:**
```
TF-IDF(t, d) = TF(t, d) × IDF(t)

Où:
- TF = Fréquence du terme dans le document
- IDF = log(N / df) où N = total documents, df = documents contenant le terme
```

**Avantages:**
- ✅ Très rapide
- ✅ Déterministe
- ✅ Bon pour les requêtes précises

**Inconvénients:**
- ❌ Ne comprend pas le contexte
- ❌ Sensible aux variations lexicales
- ❌ Précision faible (17-50%)

### BERT (Bidirectional Encoder Representations from Transformers)

**Approche:** Sémantique - Compréhension du contexte

**Architecture:**
```
Requête/Document
        ↓
   Tokenization
        ↓
   Embeddings (768D)
        ↓
  Transformer Encoder
        ↓
   Contextualized vectors
        ↓
  Similarité Cosinus
```

**Avantages:**
- ✅ Comprend le contexte et la sémantique
- ✅ Gère les variations lexicales
- ✅ Meilleure précision (70-95%)

**Inconvénients:**
- ❌ Plus lent que TF-IDF
- ❌ Nécessite plus de ressources
- ❌ Requiert un pré-entraînement

### Comparaison

| Aspect | TF-IDF | BERT |
|--------|--------|------|
| **Vitesse** | ⚡⚡⚡ Très rapide | ⚡ Modéré |
| **Contexte** | ❌ Non | ✅ Oui |
| **Flexibilité** | ❌ Rigide | ✅ Flexible |
| **Précision** | 17-50% | 70-95% |
| **Ressources** | 📱 Minimal | 💻 Modéré |
| **Scalabilité** | ✅ Excellente | ✅ Bonne |

---

## 📊 Évaluation

### Résultats des tests

Le système a été évalué sur **10 requêtes réalistes** avec un corpus de **17 documents**.

#### Métriques globales

| Métrique | TF-IDF | BERT | Fusion |
|----------|--------|------|--------|
| **Précision** | 68.08% | 75% | 85% |
| **Rappel** | 100% | 90% | 95% |
| **F1-Score** | 0.76 | 0.82 | 0.90 |

#### Performance par requête

```
🟢 Excellent (F1 ≥ 0.7)   : 7/10 requêtes (70%)
🟡 Bon (0.5 ≤ F1 < 0.7)   : 2/10 requêtes (20%)
🟠 Acceptable (0.3 ≤ F1)   : 1/10 requêtes (10%)
🔴 Faible (F1 < 0.3)       : 0/10 requêtes (0%)
```

### Test d'évaluation

```bash
# Lancer les tests d'évaluation
cd backend
python test_evaluation.py

# Génère: uploads/data/evaluation_report.json
```
### Domaines à améliorer

- [ ] Interface utilisateur mobile
- [ ] Support multilingue complet
- [ ] Authentification utilisateur
- [ ] Recommandations personnalisées
- [ ] Notification des nouvelles bourses
- [ ] Intégration avec les universités

---

## 📝 License

Ce projet est sous licence [MIT](LICENSE). Voir le fichier LICENSE pour plus de détails.

</div>
