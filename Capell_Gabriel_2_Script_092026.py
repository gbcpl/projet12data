import joblib
import pandas as pd
import sys

# Lancez l'application avec cette commande : "python application.py" ou directement via le fichier CSV avec "python application.py billets_production.csv".

# 1. Chargement du modèle

model = joblib.load("modele_billets.pkl")


# 2. Récupération du fichier fourni


if len(sys.argv) < 2:
    print("Veuillez fournir le fichier CSV.")
    print('Exemple : "python application.py billets_production.csv"')
    sys.exit()

file = sys.argv[1]

try:
    df = pd.read_csv(file, sep=",")
    
except Exception as e:
    print(f"Impossible de lire le fichier : {e}")
    sys.exit()


# 3. Vérification des colonnes selon l'ordre de l'exemple


features = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length"
]

missing_columns = [
    column for column in features
    if column not in df.columns
]

if missing_columns:
    print("Colonnes manquantes dans le fichier :")
    print(missing_columns)
    sys.exit()


# 4. Préparation des données

X = df[features]

# 5. Prédictions - Random Forest

is_genuine = model.predict(X)

df["is_genuine"] = is_genuine

# 6. Affichage des résultats

print("Résultats de l'analyse :")

for i, prediction in enumerate(is_genuine):
    
    if prediction:
        resultat = "True"
    else:
        resultat = "False"

    print(f"Billet {df.loc[i, 'id']} - {resultat}")

# 7. Sauvegarde des résultats

df.to_csv("resultats_billets.csv", sep=",", index=False)

print("Analyse terminée.")
print("Les résultats ont été enregistrés dans : resultats_billets.csv")