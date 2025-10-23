# 📝 Api analyse texte et sentiment Reddit fr

Analyse les commentaires du Reddit Français. 
Le but du projet est de récuper les derniers commentaires Reddit Fr pour les analyser, en extraire
les thèmes principaux et le sentiment qui en ressort.

## Fonctionnalités

- Analyse linguistique avec spaCy
- Extraction de mots-clés via TF-IDF
- Analyse de sentiment via camemBERT

## Technologies

- **FastAPI** : Framework
- **spaCy** : NLP
- **Pydantic** : Validation des données
- **PRAW** : Récupération de données depuis l'API Reddit
- **scikit-learn** : Extraction de mots-clés avec TF-IDF
- **Transformers (HuggingFace)** : Modèle CamemBERT pour analyse de sentiment


## Installation

```bash
# Installer modèle spaCy français
python -m spacy download fr_core_news_md
```
