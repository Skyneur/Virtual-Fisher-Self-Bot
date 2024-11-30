# Bot Discord Virtual Fisher

Ce bot Discord est conçu pour automatiser les clics sur le bouton "Fish Again" dans le canal spécifié.

## Prérequis

- Python 3.8 ou supérieur
- `discord.py` version 1.7.3 ou supérieur

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers.

2. Installez les dépendances requises en utilisant pip :

    ```sh
    pip install discord.py
    ```

3. Remplacez le token et les IDs dans le fichier `index.py` :

    ```python
    # Ton token personnel (UTILISATION À TES RISQUES ET PÉRILS)
    TOKEN = "VOTRE_TOKEN_ICI"
    CHANNEL_ID = 1231246429138452563  # ID du canal où se trouve le bot "Virtual Fisher"
    ```

## Utilisation

1. Exécutez le script `index.py` :

    ```sh
    python index.py
    ```

2. Le bot se connectera à Discord et commencera à surveiller le canal spécifié pour cliquer sur le bouton "Fish Again".

## Fonctionnalités

- Automatisation des clics sur le bouton "Fish Again".
- Affichage des messages et des embeds reçus dans le canal.
- Arrêt automatique de la tâche de pêche en cas de détection d'un captcha.

## Débogage

- Le script affiche des messages de débogage pour aider à identifier les problèmes.
- Si vous rencontrez des erreurs, vérifiez les messages de débogage dans la console.

## Avertissement

L'utilisation de self-bots est contre les conditions d'utilisation de Discord. Utilisez ce script à vos propres risques.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
