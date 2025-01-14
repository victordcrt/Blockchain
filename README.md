# Simple Blockchain

Ce projet implémente une blockchain de base avec les fonctionnalités suivantes :
- Création de blocs avec un système de proof of work
- Validation de la chaîne de blocs
- Fonctionnalités de minage

## Installation
1. Clonez ce dépôt.
2. Assurez-vous d'avoir Python 3 installé.
3. Exécutez `main.py` pour tester la blockchain.

## Structure
- `block.py` : Implémente la structure des blocs.
- `blockchain.py` : Contient la logique principale de la blockchain.
- `main.py` : Point d'entrée pour tester.

## Utilisation
Vous pouvez également tester via un navigateur ou alors Postman.
Envoyez une requête GET à /chain pour obtenir l'état actuel de la chaîne. Ou alors une requête POST à /mine avec le coprs JSON suivant pour de miner de nouveaux blocs.
```bash
{
    "data": "New block data"
}