def jeu(niveau, partie, argent):
    import pygame
    import random

    # Initialisation de Pygame
    pygame.init()

    ## Récupération des dimensions de l'écran
    info = pygame.display.Info()
    largeur_fenetre = info.current_w
    hauteur_fenetre = info.current_h

    # Création de la fenêtre du jeu
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), pygame.FULLSCREEN)
    pygame.display.set_caption("Jeu de déplacement")

    # Couleurs
    blanc = (255, 255, 255)
    noir = (0, 0, 0)
    rouge = (255, 0, 0)

    # Dimensions du personnage
    largeur_personnage = 20
    hauteur_personnage = 20

    # Position de départ du personnage
    x_personnage = largeur_fenetre // 2
    y_personnage =  hauteur_fenetre // 1.05
    position_personnage = (x_personnage, y_personnage)

    # Dimensions de la ligne d'arrivée
    largeur_ligne_arrivee = largeur_fenetre
    hauteur_ligne_arrivee = 10

    # Position de la ligne d'arrivée
    x_ligne_arrivee = 0
    y_ligne_arrivee = hauteur_fenetre // 12

    # Variables pour le déplacement du personnage
    vitesse = 3
    vers_le_haut = False
    vers_le_bas = False
    vers_la_gauche = False
    vers_la_droite = False

    #Variables dépendant du niveau
    if niveau == 1 :
        vitesse_boule = 1
        freq = 400
        gain = 10
        perte = -5
    if niveau == 2 :
        vitesse_boule = 2
        freq = 200
        gain = 20
        perte = -10
    if niveau == 3 :
        vitesse_boule = 3
        freq = 100
        gain = 40
        perte = -40
    if niveau == 4 :
        vitesse_boule = 4
        freq = 50
        gain = 80
        perte = -80

    # Classe pour les boules de feu
    class BouleDeFeu:
        def __init__(self, x, y, vitesse_boule):
            self.x = x
            self.y = y
            self.vitesse_boule = vitesse_boule / 5

        def bouger(self):
            self.y += self.vitesse_boule

        def afficher(self, fenetre):
            pygame.draw.circle(fenetre, rouge, (int(self.x), int(self.y)), 10)

    # Liste des boules de feu
    boules_de_feu = []

    # Variable pour indiquer si le joueur a perdu
    perdu = False

    # Boucle principale du jeu
    en_cours = True
    debut = pygame.time.get_ticks()
    stats = {'Niveau': niveau, 'Resultat': 'Gagne', 'Positions': [], 'Temps_pris': 0}
    # Créer une liste vide pour stocker toutes les positions prises par le personnage
    positions = [position_personnage]



    while en_cours and not perdu:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_UP:
                    vers_le_haut = True
                elif evenement.key == pygame.K_DOWN:
                    vers_le_bas = True
                elif evenement.key == pygame.K_LEFT:
                    vers_la_gauche = True
                elif evenement.key == pygame.K_RIGHT:
                    vers_la_droite = True
            elif evenement.type == pygame.KEYUP:
                if evenement.key == pygame.K_UP:
                    vers_le_haut = False
                elif evenement.key == pygame.K_DOWN:
                    vers_le_bas = False
                elif evenement.key == pygame.K_LEFT:
                    vers_la_gauche = False
                elif evenement.key == pygame.K_RIGHT:
                    vers_la_droite = False
        
        # Mise à jour de la position du personnage en fonction des touches appuyées
        x_personnage_old, y_personnage_old = position_personnage
        # Mise à jour de la position du personnage en fonction des touches appuyées
        if vers_le_haut:
            y_personnage -= vitesse
        elif vers_le_bas:
            y_personnage += vitesse
        if vers_la_gauche:
            x_personnage -= vitesse
        elif vers_la_droite:
            x_personnage += vitesse

        position_personnage = (x_personnage, y_personnage)
        # Ajouter la nouvelle position à la liste des positions prises par le personnage
        positions.append(position_personnage)

        if perdu:
            stats['resultat'] = 'Perdu'

        # Vérifier si le personnage a franchi la ligne d'arrivée
        if y_personnage < y_ligne_arrivee:
            # Mise à jour des statistiques de la partie
            stats = {'Num_partie': partie + 1, 'Niveau': niveau, 'Resultat': 'Gagne', 'Temps': pygame.time.get_ticks() - debut, 'Positions_personnage': positions}
            en_cours = False
            argent += gain
            print("Gagné !")

        # Effacement de l'écran
        fenetre.fill(blanc)

        # Dessin du personnage
        pygame.draw.rect(fenetre, noir, (x_personnage, y_personnage, largeur_personnage, hauteur_personnage))

        # Dessin de la ligne d'arrivée
        pygame.draw.rect(fenetre, rouge, (x_ligne_arrivee, y_ligne_arrivee, largeur_ligne_arrivee, hauteur_ligne_arrivee))

        # Génération des boules de feu de manière aléatoire
        temps_ecoule = pygame.time.get_ticks() - debut
        if temps_ecoule > freq:
            debut = pygame.time.get_ticks()
            x_boule_de_feu = random.randint(0, largeur_fenetre)
            y_boule_de_feu = 0
            boules_de_feu.append(BouleDeFeu(x_boule_de_feu, y_boule_de_feu, vitesse_boule))

        for boule_de_feu in boules_de_feu:
            boule_de_feu.bouger()
            boule_de_feu.afficher(fenetre)

            # Si une boule de feu atteint le personnage, le jeu s'arrête
            boule_rect = pygame.Rect(boule_de_feu.x - 10, boule_de_feu.y - 10, 20, 20) # Créer un objet Rect pour la boule de feu
            perso_rect = pygame.Rect(x_personnage, y_personnage, largeur_personnage, hauteur_personnage) # Créer un objet Rect pour le personnage
            if perso_rect.colliderect(boule_rect): # Utiliser la méthode colliderect pour détecter une collision
                # Mise à jour des statistiques de la partie
                stats = {'Num_partie': partie + 1, 'Niveau': niveau, 'Resultat': 'Perdu', 'Temps': pygame.time.get_ticks() - debut, 'Positions_personnage': positions}
                argent += perte
                perdu = True
                print("Perdu !")


        # Affichage de la fenêtre du jeu
        pygame.display.flip()

    return stats, argent
