import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

def ana_descriptives():
    # Chargement des données depuis le fichier stats.csv
    data = pd.read_csv('stats.csv')

    # Affichage des dimensions du dataframe
    print("Dimensions du dataframe : ", data.shape)

    # Calcul des statistiques descriptives pour les colonnes numériques
    num_cols = ['Age', 'Argent', 'Niveau']
    desc_stats = data[num_cols].describe()
    print(desc_stats)

    # Affichage de la distribution de chaque colonne numérique avec des courbes
    for col in ['Age', 'Argent', 'Niveau']:
        plt.plot(data[col].value_counts(normalize=True).sort_index(), '-o')
        plt.title("Répartition de la colonne " + col)
        plt.xlabel(col)
        plt.ylabel("Proportion")
        plt.show()


    # Calcul de la proportion de réponses pour chaque valeur possible de Question_1
    prop_question1 = data['Question_1'].value_counts(normalize=True)

    # Affichage du graphique en barres horizontales
    prop_question1.plot(kind='barh')
    plt.title("Répartition des sexes")
    plt.xlabel("Proportion")
    plt.ylabel("Réponse")
    plt.show()

def Modelisation_predictive():
    # Chargement des données depuis le fichier stats.csv
    data = pd.read_csv('stats.csv')

    # Conversion des valeurs de la colonne Question_1 en valeurs numériques
    data['Question_1'] = pd.Categorical(data['Question_1'], categories=['1. Femme', '2. Homme', '3. Je préfère ne pas répondre', '4. Autre'], ordered=True)
    data['Question_1'] = data['Question_1'].cat.codes + 1

    # Conversion de la colonne Resultat en valeurs numériques
    data['Resultat'] = data['Resultat'].map({'Gagne': 1, 'Perdu': 0})

    # Sélection des colonnes pour la régression
    X_reg = data[['Age', 'Argent', 'Question_1', 'Question_2', 'Question_3', 'Question_4', 'Question_5', 'Question_6', 'Question_7', 'Question_8', 'Num_partie', 'Niveau']]
    y_reg = data['Resultat']

    # Division des données en ensembles d'apprentissage et de test
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

    # Entraînement du modèle de régression
    model_reg = LinearRegression()
    model_reg.fit(X_train_reg, y_train_reg)

    # Prédiction des résultats pour l'ensemble de test
    y_pred_reg = model_reg.predict(X_test_reg)

    # Calcul des métriques de performance pour la régression
    mse_reg = mean_squared_error(y_test_reg, y_pred_reg)
    r2_reg = r2_score(y_test_reg, y_pred_reg)
    print("MSE pour la régression : ", mse_reg)
    print("R² pour la régression : ", r2_reg)

    # Sélection des colonnes pour la classification
    X_clf = data[['Age', 'Argent', 'Question_2', 'Question_3', 'Question_4', 'Question_5', 'Question_6', 'Question_7', 'Question_8', 'Num_partie', 'Niveau']]
    y_clf = data['Question_1']

    # Division des données en ensembles d'apprentissage et de test
    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

    # Entraînement du modèle de classification
    model_clf = LogisticRegression(max_iter=1000)
    model_clf.fit(X_train_clf, y_train_clf)

    # Prédiction des résultats pour l'ensemble de test
    y_pred_clf = model_clf.predict(X_test_clf)

    # Calcul des métriques de performance pour la classification
    accuracy_clf = accuracy_score(y_test_clf, y_pred_clf)
    confusion_matrix_clf = confusion_matrix(y_test_clf, y_pred_clf)
    # Affichage de la matrice de confusion pour la classification
    print("Matrice de confusion pour la classification : ")
    print(confusion_matrix_clf)
    return mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def Analyse_Resultats_PDF(mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf):
    # Création du fichier PDF
    c = canvas.Canvas("Interprétation des résultats sexes.pdf", pagesize=letter)

    # Ajout du texte dans le fichier PDF
    c.drawString(50, 750, 'RÉSULTATS DE LA MODELISATION PREDICTIVE')
    c.drawString(50, 730, '-'*50)
    c.drawString(50, 710, 'Métriques pour la régression :')
    c.drawString(50, 680, 'MSE : {}'.format(mse_reg))
    c.drawString(50, 660, 'R² : {}'.format(r2_reg))
    c.drawString(50, 630, 'Métriques pour la classification :')
    c.drawString(50, 610, 'Accuracy : {}'.format(accuracy_clf))
    c.drawString(50, 580, 'Matrice de confusion pour la classification :')
    c.drawString(50, 560, str(confusion_matrix_clf))
    c.drawString(50, 530, 'ANALYSE DES RÉSULTATS')
    c.drawString(50, 510, '-'*50)
    c.drawString(50, 490, 'La métrique MSE pour la régression représente l\'erreur quadratique moyenne entre les valeurs prédites ')
    c.drawString(50, 470, 'et les valeurs réelles. Plus la valeur est petite, plus le modèle est précis.') 
    c.drawString(50, 450, 'Ici, on obtient une MSE de {}.'.format(mse_reg))

    c.drawString(50, 410, 'La métrique R² pour la régression représente la proportion de la variance totale de la variable à expliquer') 
    c.drawString(50, 390, 'qui est expliquée par le modèle. Plus la valeur est proche de 1, plus le modèle est performant.')
    c.drawString(50, 370,  'Ici, on obtient une valeur de {}.'.format(r2_reg))

    c.drawString(50, 330, 'La métrique Accuracy pour la classification représente la proportion de prédictions correctes.' )
    c.drawString(50, 310, 'Plus la valeur est proche de 1, plus le modèle est performant. Ici, on obtient une valeur de {}.'.format(accuracy_clf)) 

    c.drawString(50, 270, 'La matrice de confusion pour la classification permet de voir le nombre de prédictions' )
    c.drawString(50, 250, 'correctes et incorrectes pour chaque classe. Ici, on cherche à prédire le sexe du participant')

    # Enregistrement du fichier PDF
    c.save()

