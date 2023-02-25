import pandas as pd
from sklearn.linear_model import LogisticRegression, LassoCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re
from fpdf import FPDF
import os

def select_features_lasso():
    # Charger les données dans un dataframe pandas
    data = pd.read_csv('stats.csv', usecols=['Age', 'Argent', 'Question_1', 'Question_2', 'Question_3', 'Question_4', 'Question_5', 'Question_6', 'Question_7', 'Question_8', 'Niveau'])

    # Convertir les réponses à la question 1 en valeurs numériques
    data['Question_1'] = data['Question_1'].replace({'1. Femme': 1, '2. Homme': 2, '3. Je préfère ne pas répondre': 3, '4. Autre': 4})

    # Sélectionner les variables d'intérêt pour la régression Lasso
    X_cols = ['Age', 'Argent', 'Question_1', 'Question_2', 'Question_3', 'Question_4', 'Question_5', 'Question_6', 'Question_7', 'Question_8']
    X = data[X_cols]
    y = data['Niveau']

    # Standardiser les données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Effectuer la régression Lasso pour sélectionner les variables les plus importantes
    lasso = LassoCV(cv=5)
    lasso.fit(X_scaled, y)

    # Extraire les noms des variables sélectionnées
    selected_features = list(X.columns[lasso.coef_ != 0])

    return X[selected_features], y


def logistic_regression():
    # Sélectionner les variables d'intérêt pour la régression logistique
    X, y = select_features_lasso()

    # Fractionner les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Créer un modèle de régression logistique
    clf = LogisticRegression(random_state=42, max_iter=1000)

    # Entraîner le modèle sur les données d'entraînement
    clf.fit(X_train, y_train)

    # Prédire les niveaux sur les données de test
    y_pred = clf.predict(X_test)

    # Calculer la précision du modèle
    accuracy = accuracy_score(y_test, y_pred)
    print("Précision du modèle : " + str(accuracy))

    return clf, accuracy

def final_model():
    # Obtenir le modèle de régression logistique et sa précision
    clf, accuracy = logistic_regression()

    # Déterminer le score de précision et le message associé
    score = round(accuracy, 3)
    if score >= 0.8:
        score_message = "Le modèle a un score de précision élevé ({score}), ce qui indique qu'il est capable de prédire avec précision le niveau de jeu dans la plupart des cas."
    else:
        score_message = "Le score de précision du modèle est relativement faible ({score}), ce qui indique qu'il peut y avoir des erreurs de prédiction dans certaines situations."

    # Créer le texte de présentation du modèle
    model_text = f"Le modèle final de régression logistique est construit à partir des variables suivantes : {select_features_lasso()[0].columns.to_list()}.\n\n"
    model_text += f"Il a été entraîné sur un ensemble de données d'entraînement, puis testé sur un ensemble de données de test. Le score de précision du modèle est de {score}.\n\n"
    model_text += score_message.format(score=score)

    # Afficher le texte de présentation du modèle
    print(model_text)

    # Retourner le modèle et sa précision
    return model_text


def enregistrer_dans_pdf(texte):
    # Créer un nouveau document PDF
    pdf = FPDF()
    pdf.add_page()

    # Définir la police et la taille de la police
    pdf.set_font("Arial", size=12)

    # Écrire le texte dans le document PDF
    pdf.multi_cell(0, 10, txt=texte)

    # Enregistrer le document PDF dans un fichier
    nom_fichier = "Prédiction niveau.pdf"
    pdf.output(nom_fichier)

    # Vérifier si le fichier a été enregistré avec succès
    if os.path.isfile(nom_fichier):
        print(f"Le fichier PDF '{nom_fichier}' a été créé avec succès.")
    else:
        print(f"Erreur : le fichier PDF '{nom_fichier}' n'a pas été créé.")
