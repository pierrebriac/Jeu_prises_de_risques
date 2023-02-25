# README

This code performs a logistic regression on a dataset of gaming-related statistics to predict the gaming level of an individual. The dataset includes variables such as age, income, and answers to several gaming-related questions.

The code first performs feature selection using Lasso regression to select the most important variables for the logistic regression. Then, the logistic regression is performed on the selected features, and the accuracy of the model is calculated. Finally, a report on the final model is generated and saved as a PDF file.

## Dependencies

- pandas
- scikit-learn
- reportlab
- fpdf
- os

## Usage

- Place the dataset file stats.csv in the same directory as the code file.
- Run the code in a Python environment.
- The final model report will be printed in the console, and a PDF file Prédiction niveau.pdf will be generated in the same directory as the code file.

# (Français)

Ce code effectue une régression logistique sur un ensemble de statistiques liées aux jeux pour prédire le niveau de jeu d'un individu. L'ensemble de données comprend des variables telles que l'âge, le revenu et les réponses à plusieurs questions liées aux jeux.

Le code effectue d'abord une sélection de fonctionnalités en utilisant la régression Lasso pour sélectionner les variables les plus importantes pour la régression logistique. Ensuite, la régression logistique est effectuée sur les fonctionnalités sélectionnées, et la précision du modèle est calculée. Enfin, un rapport sur le modèle final est généré et enregistré sous forme de fichier PDF.
## Dépendances

- pandas
- scikit-learn
- reportlab
- fpdf
- os

## Utilisation

- Placez le fichier d'ensemble de données stats.csv dans le même répertoire que le fichier de code.
- Exécutez le code dans un environnement Python.
- Le rapport final du modèle sera imprimé dans la console et un fichier PDF Prédiction niveau.pdf sera généré dans le même répertoire que le fichier de code.

