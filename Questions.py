import tkinter as tk
import csv

class Questionnaire(tk.Tk):
    def __init__(self, questions):
        super().__init__()

        # définir les questions et les options de réponse
        self.questions = questions

        # créer un dictionnaire pour stocker les réponses
        self.reponses = {}

        # créer le layout
        self.create_layout()

        # définir la fenêtre en plein écran
        self.attributes('-fullscreen', True)

    def create_layout(self):
        # créer un frame pour le layout
        frame = tk.Frame(self)
        frame.pack()

        # créer les widgets pour chaque question
        for i, question in enumerate(self.questions):
            # créer un label pour la question
            question_label = tk.Label(frame, text=question["question"])
            question_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # créer un variable pour stocker la réponse
            reponse_var = tk.StringVar()

            # créer un radio button pour chaque option
            for j, option in enumerate(question["options"]):
                radio_button = tk.Radiobutton(frame, text=option, variable=reponse_var, value=option, padx=5, pady=5)
                radio_button.grid(row=i, column=j+1, padx=5, pady=5)

            # ajouter la variable de réponse au dictionnaire avec la clé "Question_i" où i est l'indice de la question
            self.reponses[f"Question_{i+1}"] = reponse_var

        # ajouter un bouton pour soumettre les réponses
        submit_button = tk.Button(frame, text="Soumettre", command=self.submit)
        submit_button.grid(row=len(self.questions), column=0, columnspan=len(question["options"])+1, padx=5, pady=5)

    def submit(self):
        # récupérer les réponses
        for i, question in enumerate(self.questions):
            self.reponses[f"Question_{i+1}"] = self.reponses[f"Question_{i+1}"].get()

        # fermer la fenêtre
        self.destroy()

def creer_questionnaire(questions):
    questionnaire = Questionnaire(questions)
    questionnaire.mainloop()

    # retourner les réponses avec les noms de questions
    return questionnaire.reponses


