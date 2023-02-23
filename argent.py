def somme_argent(info, largeur_fenetre, hauteur_fenetre, fenetre, blanc, noir, rouge, argent):
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
        texte_regles = police_regles.render("Il vous reste : ", True, noir)
        position_regles = (largeur_fenetre // 2 - texte_regles.get_width() // 2, hauteur_fenetre // 4 - texte_regles.get_height() // 2)
        fenetre.blit(texte_regles, position_regles)

        police_info = pygame.font.SysFont(None, 40)
        texte_info1 = police_info.render(str(argent) + "$", True, noir)
        position_info1 = (largeur_fenetre // 2 - texte_info1.get_width() // 2, 2 * hauteur_fenetre // 4 - texte_info1.get_height() // 2)
        fenetre.blit(texte_info1, position_info1)

        # Affichage de la fenêtre
        pygame.display.flip()