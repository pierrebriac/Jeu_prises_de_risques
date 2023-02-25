# README

This code consists of two functions to perform descriptive analysis and predictive modeling on a dataset. The dataset is loaded from a CSV file named 'stats.csv' and contains columns such as Age, Argent, Niveau, Question_1, Question_2, etc.

## Dependencies

- pandas
- scikit-learn
- reportlab
- matplotlib

### ana_descriptives()

This function performs the following tasks:

- Load the dataset from the CSV file
- Display the dimensions of the dataframe
- Calculate the descriptive statistics for the numerical columns
- Display the distribution of each numerical column using curves
- Calculate the proportion of responses for each possible value of Question_1
- Display the horizontal bar chart for the distribution of sexes.

### Modelisation_predictive()

This function performs the following tasks:

- Load the dataset from the CSV file
- Convert the values of the column Question_1 into numerical values
- Convert the column Resultat into numerical values
- Select the columns for regression and classification
- Divide the data into training and test sets
- Train the regression and classification models
- Predict the results for the test sets
- Calculate the performance metrics for regression and classification
- Return the metrics.

### Analyse_Resultats_PDF(mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf)

This function takes the performance metrics returned by Modelisation_predictive() and generates a PDF file with the following contents:

- Results of predictive modeling
- Performance metrics for regression and classification
- Analysis of the results.
    
# (Français)

Ce code se compose de deux fonctions pour effectuer une analyse descriptive et une modélisation prédictive sur un ensemble de données. L'ensemble de données est chargé à partir d'un fichier CSV nommé 'stats.csv' et contient des colonnes telles que Age, Argent, Niveau, Question_1, Question_2, etc.
## Dépendances

- pandas
- scikit-learn
- reportlab
- matplotlib

### ana_descriptives()

Cette fonction effectue les tâches suivantes :

- Charge l'ensemble de données à partir du fichier CSV
- Affiche les dimensions du dataframe
- Calcule les statistiques descriptives pour les colonnes numériques
- Affiche la distribution de chaque colonne numérique à l'aide de courbes
- Calcule la proportion de réponses pour chaque valeur possible de Question_1
- Affiche le graphique en barres horizontales pour la répartition des sexes.

### Modelisation_predictive()

Cette fonction effectue les tâches suivantes :

- Charge l'ensemble de données à partir du fichier CSV
- Convertit les valeurs de la colonne Question_1 en valeurs numériques
- Convertit la colonne Resultat en valeurs numériques
- Sélectionne les colonnes pour la régression et la classification
- Divise les données en ensembles d'apprentissage et de test
- Entraîne les modèles de régression et de classification
- Prédit les résultats pour les ensembles de test
- Calcule les métriques de performance pour la régression et la classification
- Retourne les métriques.
### Analyse_Resultats_PDF(mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf)

Cette fonction prend les métriques de performance renvoyées par Modelisation_predictive() et génère un fichier PDF avec les contenus suivants :

- Résultats de la modélisation prédictive
- Métriques de performance pour la régression
- Analyse des résultats.
