import pygame
import random
from Fonction_jeu import jeu
import csv
from Questions import creer_questionnaire
import curses
from info_part import demander_age, id_participant
from liste_questions import liste_questions
from consignes import afficher_regles
from argent import somme_argent
from Predict_sexe_logistique import ana_descriptives, Modelisation_predictive, Analyse_Resultats_PDF
from Predict_niveau_logistique import select_features_lasso, logistic_regression, final_model, enregistrer_dans_pdf
argent = 100
id_participant = id_participant()
age_utilisateur = demander_age()

questions = liste_questions()

reponses = creer_questionnaire(questions)

def enregistrer_stats(stats, reponses, age_utilisateur, id_participant, argent):
    with open('stats.csv', 'a', newline='') as file:
        fieldnames = ["ID", "Age", "Argent"] + ["Question_{}".format(i+1) for i in range(len(reponses))]
        fieldnames += list(stats.keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        row = {"ID": id_participant, "Age": age_utilisateur, "Argent": argent, **reponses, **stats}
        writer.writerow(row)


# Initialisation de Pygame
pygame.init()


# Récupération des dimensions de l'écran
info = pygame.display.Info()
largeur_fenetre = info.current_w
hauteur_fenetre = info.current_h

# Création de la fenêtre du jeu en plein écran
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), pygame.FULLSCREEN)

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Polices de caractères
police_titre = pygame.font.SysFont(None, 100)
police_bouton = pygame.font.SysFont(None, 50)

# Textes des boutons
texte_bouton1 = police_bouton.render("Niveau 1", True, blanc)
texte_bouton2 = police_bouton.render("Niveau 2", True, blanc)
texte_bouton3 = police_bouton.render("Niveau 3", True, blanc)
texte_bouton4 = police_bouton.render("Niveau 4", True, blanc)

# Position des boutons
position_bouton1 = (largeur_fenetre // 4 - texte_bouton1.get_width() // 2, hauteur_fenetre // 2 - 50)
position_bouton2 = (largeur_fenetre // 2 - texte_bouton2.get_width() // 2, hauteur_fenetre // 2 - 50)
position_bouton3 = (3 * largeur_fenetre // 4 - texte_bouton3.get_width() // 2, hauteur_fenetre // 2 - 50)
position_bouton4 = (largeur_fenetre // 2 - texte_bouton4.get_width() // 2, hauteur_fenetre // 2 + 50)

afficher_regles(info, largeur_fenetre, hauteur_fenetre, fenetre, blanc, noir, rouge)

# Boucle principale du jeu
for i in range(10): # boucle pour lancer le jeu x fois
    en_cours = True
    valeur_retour = None # Initialisation de la valeur de retour
    while en_cours:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.MOUSEBUTTONUP:
                x_souris, y_souris = pygame.mouse.get_pos()
                if position_bouton1[0] <= x_souris <= position_bouton1[0] + texte_bouton1.get_width() and \
                        position_bouton1[1] <= y_souris <= position_bouton1[1] + texte_bouton1.get_height():
                    valeur_retour = 1
                elif position_bouton2[0] <= x_souris <= position_bouton2[0] + texte_bouton2.get_width() and \
                        position_bouton2[1] <= y_souris <= position_bouton2[1] + texte_bouton2.get_height():
                    valeur_retour = 2
                elif position_bouton3[0] <= x_souris <= position_bouton3[0] + texte_bouton3.get_width() and \
                        position_bouton3[1] <= y_souris <= position_bouton3[1] + texte_bouton3.get_height():
                    valeur_retour = 3
                elif position_bouton4[0] <= x_souris <= position_bouton4[0] + texte_bouton4.get_width() and \
                        position_bouton4[1] <= y_souris <= position_bouton4[1] + texte_bouton4.get_height():
                    valeur_retour = 4

        if valeur_retour is not None: # Vérification que la valeur de retour a été modifiée
            # Appel de la fonction jeu()
            stats, argent = jeu(valeur_retour, i, argent)
            somme_argent(info, largeur_fenetre, hauteur_fenetre, fenetre, blanc, noir, rouge, argent)
            enregistrer_stats(stats, reponses, age_utilisateur, id_participant, argent)
            en_cours = False

        # Effacement de l'écran
        fenetre.fill(blanc)

        # Affichage du titre
        texte_titre = police_titre.render("Menu", True, noir)
        position_titre = (largeur_fenetre // 2 - texte_titre.get_width() // 2, hauteur_fenetre // 4 - texte_titre.get_height() // 2)
        fenetre.blit(texte_titre, position_titre)

        # Affichage des boutons
        pygame.draw.rect(fenetre, rouge, (position_bouton1[0] - 10, position_bouton1[1] - 10, texte_bouton1.get_width() + 20, texte_bouton1.get_height() + 20))
        fenetre.blit(texte_bouton1, position_bouton1)

        pygame.draw.rect(fenetre, rouge, (position_bouton2[0] - 10, position_bouton2[1] - 10, texte_bouton2.get_width() + 20, texte_bouton2.get_height() + 20))
        fenetre.blit(texte_bouton2, position_bouton2)

        pygame.draw.rect(fenetre, rouge, (position_bouton3[0] - 10, position_bouton3[1] - 10, texte_bouton3.get_width() + 20, texte_bouton3.get_height() + 20))
        fenetre.blit(texte_bouton3, position_bouton3)

        pygame.draw.rect(fenetre, rouge, (position_bouton4[0] - 10, position_bouton4[1] - 10, texte_bouton4.get_width() + 20, texte_bouton4.get_height() + 20))
        fenetre.blit(texte_bouton4, position_bouton4)

        # Affichage de la fenêtre du jeu
        pygame.display.flip()

pygame.quit()

print("Vous avez gagné : " + str(argent) + "$")

# Résultats :
ana_descriptives()
mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf = Modelisation_predictive()
Analyse_Resultats_PDF(mse_reg, r2_reg, accuracy_clf, confusion_matrix_clf)

texte_inter = final_model()
enregistrer_dans_pdf(texte_inter)