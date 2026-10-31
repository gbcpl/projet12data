# Projet 12 — Détectez des faux billets avec Python

## Présentation du projet

L'Organisation nationale de lutte contre le faux-monnayage (ONCFM) souhaite exploiter les données pour déterminer si un billet est authentique ou contrefait.

Le projet repose sur un jeu de données de 1 500 billets, dont 1 000 authentiques et 500 faux. Chaque billet est décrit par six caractéristiques géométriques : sa longueur, sa diagonale, la hauteur mesurée à gauche et à droite, ainsi que les marges supérieure et inférieure.

L'objectif est de construire un modèle de Machine Learning capable de classifier les billets, puis de développer un script Python permettant d'appliquer ce modèle à de nouvelles données.

## Objectifs

- Explorer et préparer les données de billets.
- Identifier les caractéristiques les plus associées à l'authenticité.
- Entraîner et comparer plusieurs modèles de classification.
- Évaluer les performances des modèles avec différentes métriques.
- Sélectionner le modèle le plus adapté à la détection des faux billets.
- Sauvegarder le modèle et l'intégrer dans un script Python utilisable sur de nouveaux fichiers CSV.

## Méthodologie

1. **Analyse exploratoire** : étude des données, des valeurs manquantes et des différences entre billets authentiques et contrefaits.
2. **Analyse des corrélations** : exploration des relations entre les caractéristiques géométriques et la variable cible `is_genuine`.
3. **Prétraitement** : suppression des lignes dépourvues de la mesure `margin_low`, séparation des variables explicatives et de la cible, puis standardisation des données lorsque nécessaire.
4. **Séparation des données** : constitution d'un jeu d'entraînement et d'un jeu de test, avec une répartition de 80 % et 20 %.
5. **Modélisation** : entraînement de modèles de régression logistique, K plus proches voisins (KNN) et Random Forest, ainsi qu'une exploration de méthodes de clustering.
6. **Évaluation** : comparaison des modèles à l'aide de l'accuracy, de la précision, du rappel, du F1-score et de la ROC-AUC.
7. **Déploiement** : création d'un pipeline intégrant la standardisation et la Random Forest, puis sauvegarde du modèle avec Joblib et développement d'un script de prédiction.

## Résultats clés

L'analyse exploratoire met en évidence plusieurs relations entre les caractéristiques géométriques et l'authenticité des billets.

Parmi les variables étudiées, la longueur présente une corrélation positive importante avec l'authenticité, tandis que la marge inférieure présente une corrélation négative importante. La diagonale est, quant à elle, beaucoup moins corrélée à la variable cible.

Trois modèles de classification ont été comparés :

- **Régression logistique** : modèle de référence pour la classification binaire.
- **KNN** : classification fondée sur la proximité entre les observations.
- **Random Forest** : ensemble d'arbres de décision permettant de modéliser des relations potentiellement non linéaires.

Les trois modèles obtiennent des performances proches de 99 % sur les données de test. La Random Forest est retenue en raison de son score ROC-AUC légèrement supérieur dans les résultats du projet.

Le modèle final est intégré dans un pipeline comprenant la standardisation et la classification. Il est ensuite sauvegardé afin de pouvoir réaliser des prédictions sur de nouveaux billets.

## Outils et technologies

- **Python** : développement et automatisation des traitements.
- **Jupyter Notebook** : analyse exploratoire et expérimentation.
- **Pandas et NumPy** : manipulation des données.
- **Matplotlib et Seaborn** : visualisation et analyse des relations entre variables.
- **Scikit-learn** : prétraitement, entraînement, classification et évaluation des modèles.
- **Joblib** : sauvegarde et chargement du modèle entraîné.
- **CSV** : format d'entrée et de sortie du script de prédiction.

## Livrables

- [Notebook d'analyse](./Capell_Gabriel_1_Notebook_analyse_092026.ipynb)
- [Script Python de prédiction](./Capell_Gabriel_2_Script_092026.py)
- [Support de présentation](./Capell_Gabriel_3_Support_092026.pptx)

## Compétences développées

- Exploration et préparation de données.
- Analyse de corrélations et visualisation statistique.
- Prétraitement et standardisation des variables.
- Classification supervisée avec Scikit-learn.
- Comparaison et évaluation de modèles de Machine Learning.
- Analyse des matrices de confusion et des courbes ROC.
- Construction et sauvegarde d'un pipeline de prédiction.
- Automatisation de prédictions à partir d'un fichier CSV.

## Conclusion

Ce projet m'a permis de mettre en pratique une démarche complète de Machine Learning, depuis l'analyse exploratoire jusqu'à l'intégration d'un modèle dans un script Python.

La comparaison de plusieurs algorithmes a permis de sélectionner une Random Forest présentant de très bonnes performances sur les données de test. Le modèle sauvegardé peut ensuite être utilisé pour classifier de nouveaux billets à partir de leurs caractéristiques géométriques.

---

**Domaine :** Data Analytics et Machine Learning  
**Outils principaux :** Python, Pandas, Scikit-learn, Joblib  
**Type de projet :** Classification supervisée et détection de faux billets  
**Formation :** Data Analyst  
**Dépôt GitHub :** [projet12data](https://github.com/gbcpl/projet12data)
