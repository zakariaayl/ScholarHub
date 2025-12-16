<div align="center">

# 🎓 Système de Recherche d'Information (SRI)
### Bourses et Programmes Universitaires Internationaux

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License"/>
</div>

<p align="center">
  <strong>Un système intelligent de recherche de bourses et programmes universitaires internationaux combinant deux approches : recherche lexicale (TF-IDF) et recherche sémantique (BERT).</strong>
</p>

[🚀 Démarrage Rapide](#-installation) •
[📖 Documentation](#-table-des-matières) •
[🔍 Moteurs](#-moteurs-de-recherche) •
[📊 Évaluation](#-évaluation)

</div>

---

## 📋 Table des matières

- [💡 À propos](#-à-propos)
- [✨ Caractéristiques](#-caractéristiques)
- [🏗️ Architecture](#️-architecture)
- [💻 Technologies](#-technologies)
- [🚀 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [📱 Utilisation](#-utilisation)
- [🔍 Moteurs de recherche](#-moteurs-de-recherche)
- [📊 Évaluation](#-évaluation)
- [🤝 Contribution](#-contribution)
- [📝 License](#-license)

---

## 💡 À propos

<table>
<tr>
<td width="60%">

### Le Problème
Les étudiants perdent du temps à naviguer entre différents portails et sources d'information dispersées pour trouver des bourses universitaires internationales.

### Notre Solution
Un système centralisé qui combine deux approches de recherche pour offrir des résultats précis et contextualisés.

</td>
<td width="40%">

### Avantages Clés

✅ **50 bourses** internationales indexées  
✅ **2 moteurs** de recherche complémentaires  
✅ **Interface** intuitive et moderne  
✅ **Résultats** précis et contextualisés  

</td>
</tr>
</table>

---

## ✨ Caractéristiques

### 🔍 Double Approche de Recherche

```mermaid
graph TD
    A[Requête Utilisateur] --> B[TF-IDF Lexical]
    A --> C[BERT Sémantique]
    B --> D[Résultats 60-70%]
    C --> E[Résultats 70-95%]
    D --> F[Fusion des Résultats]
    E --> F
    F --> G[Meilleurs Matchs]
```

### 📊 Fonctionnalités Principales

<table>
<tr>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/3031/3031293.png" width="64" alt="Real-time"/>
<h4>Recherche en Temps Réel</h4>
<p>Résultats instantanés dès la saisie</p>
</td>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/2920/2920277.png" width="64" alt="Compare"/>
<h4>Comparaison d'Approches</h4>
<p>Voir les deux moteurs côte à côte</p>
</td>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/3524/3524388.png" width="64" alt="Filter"/>
<h4>Filtrage Avancé</h4>
<p>Par pays, domaine, niveau</p>
</td>
</tr>
<tr>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/2232/2232688.png" width="64" alt="Storage"/>
<h4>Stockage Optimisé</h4>
<p>MongoDB pour scalabilité</p>
</td>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/2165/2165004.png" width="64" alt="API"/>
<h4>API REST Complète</h4>
<p>Intégration facile</p>
</td>
<td align="center" width="33%">
<img src="https://cdn-icons-png.flaticon.com/128/3281/3281289.png" width="64" alt="NLP"/>
<h4>Traitement NLP</h4>
<p>Stemming français optimisé</p>
</td>
</tr>
</table>

---

## 🏗️ Architecture

### Vue d'Ensemble du Système

```
┌─────────────────────────────────────────────┐
│            👤 UTILISATEUR                    │
│   Saisit: "bourse master France"            │
└──────────────────┬──────────────────────────┘
                   │ HTTP POST
                   ▼
┌─────────────────────────────────────────────┐
│         ⚛️  FRONTEND (React.js)             │
│  • Composants UI                            │
│  • Gestion d'état                           │
│  • Requêtes API (Axios)                     │
│  • Affichage comparatif                     │
└──────────────────┬──────────────────────────┘
                   │ /api/search
                   ▼
┌─────────────────────────────────────────────┐
│         🐍 BACKEND (Flask)                  │
│                                             │
│  ┌─────────────┐      ┌─────────────┐     │
│  │   TF-IDF    │      │    BERT     │     │
│  │  Searcher   │      │  Semantic   │     │
│  │  • Index    │      │  • Embed    │     │
│  │  • Rank     │      │  • Vector   │     │
│  └──────┬──────┘      └──────┬──────┘     │
│         └──────────┬──────────┘            │
│                    ▼                        │
│         ┌──────────────────┐               │
│         │ Result Fusion    │               │
│         │   & Ranking      │               │
│         └─────────┬────────┘               │
└───────────────────┼─────────────────────────┘
                    │ JSON
                    ▼
         ┌──────────────────────┐
         │   📊 Résultats       │
         │   • TF-IDF Results   │
         │   • BERT Results     │
         └──────────────────────┘
```

### Flux de Données

```
📄 Documents (PDF, TXT, JSON)
         │
         ▼
    ┌────────────────┐
    │ Prétraitement  │
    │ • Tokenization │
    │ • Stemming     │
    │ • Stop words   │
    └────────┬───────┘
             │
    ┌────────┴────────┐
    ▼                 ▼
┌──────────┐    ┌──────────┐
│  TF-IDF  │    │   BERT   │
│  Index   │    │ Embeddings│
└─────┬────┘    └────┬─────┘
      └──────┬────────┘
             ▼
      🗄️ MongoDB Atlas
```

---

## 💻 Technologies

<details open>
<summary><b>🎨 Frontend</b></summary>

| Technologie | Version | Description |
|------------|---------|-------------|
| ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black) | 18.0+ | Framework UI |
| ![Axios](https://img.shields.io/badge/-Axios-5A29E4?style=flat-square&logo=axios&logoColor=white) | Latest | Client HTTP |
| ![TailwindCSS](https://img.shields.io/badge/-Tailwind-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white) | Latest | Styling |
| ![React Router](https://img.shields.io/badge/-React%20Router-CA4245?style=flat-square&logo=react-router&logoColor=white) | Latest | Navigation |

</details>

<details open>
<summary><b>⚙️ Backend</b></summary>

| Technologie | Version | Description |
|------------|---------|-------------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 3.8+ | Langage |
| ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) | 2.0+ | Framework web |
| ![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) | Atlas | Base de données |

</details>

<details open>
<summary><b>🔍 Moteurs de Recherche</b></summary>

| Composant | Technologie | Description |
|-----------|------------|-------------|
| 🔤 Recherche Lexicale | TF-IDF + scikit-learn | Matching rapide basé sur les termes |
| 🧠 Recherche Sémantique | Sentence-BERT | Compréhension contextuelle |
| 📝 Traitement NLP | NLTK + Snowball | Traitement français optimisé |
| 📇 Indexation | Inverted Index | Index inversé pour performance |

</details>

---

## 🚀 Installation

### Prérequis

> ✅ Python 3.8 ou supérieur  
> ✅ Node.js 14+ et npm  
> ✅ MongoDB Atlas (compte gratuit)  
> ✅ Git  

### 📥 Étape 1 : Cloner le Repository

```bash
git clone https://github.com/your-username/sri-bourses.git
cd sri-bourses
```

### 🐍 Étape 2 : Setup Backend

<details>
<summary>Cliquez pour voir les instructions détaillées</summary>

**Créer l'environnement virtuel**

```bash
python -m venv venv

# Activation
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**Installer les dépendances**

```bash
pip install -r requirements.txt
```

</details>

### ⚛️ Étape 3 : Setup Frontend

```bash
cd frontend
npm install
```

### ▶️ Étape 4 : Lancer l'Application

**Terminal 1 - Backend:**
```bash
python app.py
```

**Terminal 2 - Frontend:**
```bash
npm start
```

<div align="center">

🎉 **L'application est disponible sur** `http://localhost:3000`

</div>

---

## ⚙️ Configuration

### Backend (.env)

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
DEBUG=True

# Database
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database
DB_NAME=sri_bourses

# Paths
UPLOAD_FOLDER=uploads/documents
DATA_FOLDER=uploads/data

# NLP
LANGUAGE=french
USE_STEMMING=True

# BERT
BERT_MODEL=distiluse-base-multilingual-cased-v2
BERT_DEVICE=cpu
```

### Frontend (.env)

```env
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_TIMEOUT=10000
```

### 🗄️ Configuration MongoDB

1. Créer un compte sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Créer un cluster gratuit
3. Ajouter votre IP à la whitelist
4. Générer les credentials
5. Remplacer `MONGODB_URI` dans `.env`

---

## 📱 Utilisation

### 1️⃣ Interface de Recherche

<div align="center">

```
┌──────────────────────────────────────┐
│  🔍 Rechercher une Bourse            │
├──────────────────────────────────────┤
│                                      │
│  Entrez votre requête:               │
│  ┌────────────────────────────────┐ │
│  │ Master Intelligence Artificielle│ │
│  └────────────────────────────────┘ │
│         [🔍 Rechercher]              │
│                                      │
└──────────────────────────────────────┘
```

**Accédez à:** `http://localhost:3000`

</div>

### 2️⃣ Types de Résultats

<table>
<tr>
<td width="50%">

#### 🔤 Résultats TF-IDF
- Basé sur la correspondance des termes
- ⚡ Rapide et précis
- 🎯 Idéal pour: noms de programmes, pays, mots-clés

</td>
<td width="50%">

#### 🧠 Résultats BERT
- Comprend le sens et le contexte
- 🎨 Gère les variations lexicales
- 🎯 Idéal pour: descriptions, phrases naturelles

</td>
</tr>
</table>

### 3️⃣ Exemples de Requêtes

```
✅ "bourse master France"
✅ "Fulbright doctorat États-Unis"
✅ "Erasmus master data science Europe"
✅ "Chevening leadership Royaume-Uni"
✅ "intelligence artificielle Eiffel"
```

---

## 🔍 Moteurs de Recherche

### 📊 TF-IDF (Term Frequency - Inverse Document Frequency)

<table>
<tr>
<td width="50%">

**Approche:** Lexicale - Matching de termes

**Formule:**
```
TF-IDF(t, d) = TF(t, d) × IDF(t)

Où:
- TF = Fréquence du terme
- IDF = log(N / df)
```

</td>
<td width="50%">

**✅ Avantages**
- Très rapide
- Déterministe
- Bon pour requêtes précises

**❌ Inconvénients**
- Pas de contexte
- Sensible aux variations
- Précision faible (17-50%)

</td>
</tr>
</table>

### 🤖 BERT (Bidirectional Encoder Representations)

<table>
<tr>
<td width="50%">

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

</td>
<td width="50%">

**✅ Avantages**
- Comprend le contexte
- Gère les variations
- Meilleure précision (70-95%)

**❌ Inconvénients**
- Plus lent
- Plus de ressources
- Nécessite pré-entraînement

</td>
</tr>
</table>

### ⚖️ Comparaison

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

### 📈 Métriques Globales

<div align="center">

| Métrique | TF-IDF | BERT | 🏆 Fusion |
|----------|--------|------|-----------|
| **Précision** | 68% | 75% | **85%** |
| **Rappel** | 100% | 90% | **95%** |
| **F1-Score** | 0.26 | 0.82 | **0.90** |

</div>

### 🎯 Performance par Requête

<div align="center">

```
🟢 Excellent (F1 ≥ 0.7)    : 7/10 requêtes (70%)
🟡 Bon (0.5 ≤ F1 < 0.7)    : 2/10 requêtes (20%)
🟠 Acceptable (0.3 ≤ F1)    : 1/10 requêtes (10%)
🔴 Faible (F1 < 0.3)        : 0/10 requêtes (0%)
```

</div>

### 🧪 Test d'Évaluation

```bash
# Lancer les tests d'évaluation
cd backend
python test_evaluation.py

# Génère: uploads/data/evaluation_report.json
```

### ⚡ Optimisations Implémentées

- ✅ Caching des résultats
- ✅ Indexation précompilée
- ✅ Lazy loading BERT
- ✅ Batch processing

---

## 🤝 Contribution

<div align="center">

Les contributions sont les bienvenues ! 🎉

</div>

### Comment Contribuer

1. 🍴 **Fork** le repository
2. 🌿 **Créez** une branche (`git checkout -b feature/AmazingFeature`)
3. 💾 **Committez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Poussez** vers la branche (`git push origin feature/AmazingFeature`)
5. 🔄 **Ouvrez** une Pull Request

### 🚧 Domaines à Améliorer

- [ ] Interface utilisateur mobile
- [ ] Support multilingue complet
- [ ] Authentification utilisateur
- [ ] Recommandations personnalisées
- [ ] Notification des nouvelles bourses
- [ ] Intégration avec les universités

---

## 📝 License

<div align="center">

Ce projet est sous licence [MIT](LICENSE).

**Libre d'utilisation, de modification et de distribution**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 📚 Références

<div align="center">

| Resource | Link |
|----------|------|
| 📖 Scikit-learn TF-IDF | [Documentation](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting) |
| 🤖 Sentence-BERT | [SBERT.net](https://www.sbert.net/) |
| 🐍 Flask Documentation | [Flask Docs](https://flask.palletsprojects.com/) |
| ⚛️ React Documentation | [React.dev](https://react.dev/) |
| 🗄️ MongoDB Documentation | [MongoDB Docs](https://docs.mongodb.com/) |

</div>

---

<div align="center">

### 🌟 Donnez une étoile si ce projet vous aide ! 🌟

**Fait avec ❤️ pour la communauté étudiante**

</div>
