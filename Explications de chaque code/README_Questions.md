# README

## Introduction

This code defines a Questionnaire class that creates a GUI interface using tkinter to display a set of questions with radio button options for each question. It also provides a method to submit the answers and returns a dictionary with the responses.

## Requirements

This code requires Python 3 and the tkinter library, which is typically included in standard Python installations.

## How to use

The creer_questionnaire function can be called with a list of dictionaries where each dictionary represents a question and its options. The Questionnaire class then creates a GUI interface with radio button options for each question. Once the user submits the answers, the function returns a dictionary with the responses.

## Class methods
### __init__(self, questions)

The constructor for the Questionnaire class takes a list of dictionaries representing the questions and options. It initializes the questions and options, creates a dictionary to store the responses, creates the layout, and sets the window to fullscreen.

### create_layout(self)

This method creates the layout for the GUI interface, including the questions, options, and submit button.

### submit(self)

This method is called when the user clicks the submit button. It retrieves the selected options for each question and stores them in the reponses dictionary. It then closes the window.

## Function
### creer_questionnaire(questions)

This function takes a list of dictionaries representing the questions and options, creates a Questionnaire object, and displays the GUI interface. Once the user submits the answers, it returns a dictionary with the responses.

# (FRANÇAIS)

## Introduction

Ce code définit une classe Questionnaire qui crée une interface GUI en utilisant tkinter pour afficher un ensemble de questions avec des options de boutons radio pour chaque question. Il fournit également une méthode pour soumettre les réponses et renvoie un dictionnaire avec les réponses.

## Exigences

Ce code nécessite Python 3 et la bibliothèque tkinter, qui est généralement incluse dans les installations standard de Python.
Comment utiliser

La fonction creer_questionnaire peut être appelée avec une liste de dictionnaires où chaque dictionnaire représente une question et ses options. La classe Questionnaire crée ensuite une interface GUI avec des options de bouton radio pour chaque question. Une fois que l'utilisateur a soumis les réponses, la fonction renvoie un dictionnaire avec les réponses.

## Méthodes de classe
### __init__(self, questions)

Le constructeur de la classe Questionnaire prend une liste de dictionnaires représentant les questions et les options. Il initialise les questions et les options, crée un dictionnaire pour stocker les réponses, crée la mise en page pour l'interface GUI et configure la fenêtre en mode plein écran.

### create_layout(self)

Cette méthode crée la mise en page pour l'interface GUI, y compris les questions, les options et le bouton de soumission.

### submit(self)

Cette méthode est appelée lorsque l'utilisateur clique sur le bouton de soumission. Elle récupère les options sélectionnées pour chaque question et les stocke dans le dictionnaire reponses. Elle ferme ensuite la fenêtre.

## Fonction

### creer_questionnaire(questions)

Cette fonction prend une liste de dictionnaires représentant les questions et les options, crée un objet Questionnaire et affiche l'interface GUI. Une fois que l'utilisateur a soumis les réponses, elle renvoie un dictionnaire avec les réponses.
