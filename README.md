# fastapi-wol/fastapi-wol/README.md

# Projet Wake on LAN avec FastAPI

Ce projet permet d'envoyer des signaux Wake on LAN (WOL) à des machines spécifiées via une API FastAPI.

## Structure du projet

- `src/data/machines.json` : Contient les données des machines au format JSON, incluant les noms et adresses MAC des machines à réveiller.
- `src/wake_on_lan.py` : Définit un routeur FastAPI pour gérer les requêtes de réveil sur LAN. Il contient les fonctions `load_machines`, `wake_on_lan`, et `send_wol`.
- `src/main.py` : Point d'entrée de l'application FastAPI. Importe le routeur de `wake_on_lan.py` et démarre le serveur.
- `Dockerfile` : Instructions pour construire l'image Docker de l'application. Spécifie l'environnement d'exécution, copie les fichiers nécessaires et installe les dépendances.
- `requirements.txt` : Liste les dépendances Python nécessaires pour le projet, y compris FastAPI et d'autres bibliothèques requises.

## Installation

1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd fastapi-wol
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Exécution

Pour exécuter l'application localement, utilisez la commande suivante :
```
uvicorn src.main:app --reload
```

## Déploiement avec Docker

Pour construire et exécuter l'application dans un conteneur Docker, utilisez les commandes suivantes :

1. Construisez l'image Docker :
   ```
   docker build -t fastapi-wol .
   ```

2. Exécutez le conteneur :
   ```
   docker run -d -p 8000:8000 fastapi-wol
   ```

L'application sera accessible à l'adresse `http://localhost:8000`.

## Utilisation de l'API

Pour réveiller une machine, envoyez une requête POST à l'endpoint suivant :
```
POST /wake-on-lan/{machine_name}
```

Remplacez `{machine_name}` par le nom de la machine que vous souhaitez réveiller.