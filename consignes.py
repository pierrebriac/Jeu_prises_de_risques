def afficher_regles(info, largeur_fenetre, hauteur_fenetre, fenetre, blanc, noir, rouge):
    import pygame
    en_cours = True
    while en_cours:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_SPACE:
                    en_cours = False

        # Effacement de l'écran
        fenetre.fill(blanc)

        # Affichage du texte
        police_regles = pygame.font.SysFont(None, 60)
        texte_regles = police_regles.render("Règles du jeu :", True, noir)
        position_regles = (largeur_fenetre // 2 - texte_regles.get_width() // 2, hauteur_fenetre // 4 - texte_regles.get_height() // 2)
        fenetre.blit(texte_regles, position_regles)

        police_info = pygame.font.SysFont(None, 40)
        texte_info1 = police_info.render("Vous commencez le jeu avec 100$.", True, noir)
        position_info1 = (largeur_fenetre // 2 - texte_info1.get_width() // 2, 2 * hauteur_fenetre // 4 - texte_info1.get_height() // 2)
        fenetre.blit(texte_info1, position_info1)

        texte_info2 = police_info.render("Le but du jeu est de gagner de l'argent en répondant aux questions.", True, noir)
        position_info2 = (largeur_fenetre // 2 - texte_info2.get_width() // 2, 2 * hauteur_fenetre // 4 + texte_info1.get_height())
        fenetre.blit(texte_info2, position_info2)

        texte_info3 = police_info.render("Vous avez le choix entre quatre niveaux de difficulté.", True, noir)
        position_info3 = (largeur_fenetre // 2 - texte_info3.get_width() // 2, 2 * hauteur_fenetre // 4 + 2 * texte_info1.get_height())
        fenetre.blit(texte_info3, position_info3)

        texte_info4 = police_info.render("Pour répondre, vous devez cliquer sur l'une des options proposées.", True, noir)
        position_info4 = (largeur_fenetre // 2 - texte_info4.get_width() // 2, 2 * hauteur_fenetre // 4 + 3 * texte_info1.get_height())
        fenetre.blit(texte_info4, position_info4)

        texte_info5 = police_info.render("Plus le niveau sélectionné est élevé plus il est difficile, mais il rapportera plus d'argent si vous le réussissez", True, noir)
        position_info5 = (largeur_fenetre // 2 - texte_info5.get_width() // 2, 2 * hauteur_fenetre // 4 + 4 * texte_info1.get_height())
        fenetre.blit(texte_info5, position_info5)

        texte_info6 = police_info.render("En revanche si vous perdez, vous aller perdre plus.", True, noir)
        position_info6 = (largeur_fenetre // 2 - texte_info6.get_width() // 2, 2 * hauteur_fenetre // 4 + 5 * texte_info6.get_height())
        fenetre.blit(texte_info6, position_info6)

        texte_info7 = police_info.render("Niveau 1 = +10$ ou -5$, Niveau 2 = +20$ ou - 10$, Niveau 3 = +40$ ou -40$, Niveau 4 = +80$ ou - 80$", True, noir)
        position_info7 = (largeur_fenetre // 2 - texte_info7.get_width() // 2, 2 * hauteur_fenetre // 4 + 7 * texte_info7.get_height())
        fenetre.blit(texte_info7, position_info7)

        texte_info8 = police_info.render("Appuyez sur la barre d'espace pour commencer.", True, noir)
        position_info8 = (largeur_fenetre // 2 - texte_info8.get_width() // 2, 3 * hauteur_fenetre // 4 - texte_info8.get_height() // 2)
        fenetre.blit(texte_info8, position_info8)

        # Affichage de la fenêtre
        pygame.display.flip()
