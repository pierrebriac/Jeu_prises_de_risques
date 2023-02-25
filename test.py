import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

# Mes programmes
from Predict_sexe_logistique import ana_descriptives, Modelisation_predictive, Analyse_Resultats_PDF
from Predict_niveau_logistique import Modelisation_predictive_niveau

ana_descriptives()
mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf = Modelisation_predictive()
Analyse_Resultats_PDF(mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf)

#Modelisation_predictive_niveau()