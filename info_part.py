import curses

def demander_age():
    # Initialiser la bibliothèque curses
    screen = curses.initscr()

    # Effacer l'écran
    screen.clear()

    # Récupérer les dimensions de l'écran
    height, width = screen.getmaxyx()

    # Calculer la position du message
    x = width // 2 - len("Quel est votre âge ?") // 2
    y = height // 2

    # Afficher le message
    screen.addstr(y, x, "Quel est votre âge ?")

    # Récupérer l'âge entré par l'utilisateur
    age = screen.getstr(y+1, x)

    # Fermer la fenêtre
    curses.endwin()

    # Retourner l'âge sous forme de chaîne de caractères
    return age.decode("utf-8")

def id_participant():
    # Initialiser la bibliothèque curses
    screen = curses.initscr()

    # Effacer l'écran
    screen.clear()

    # Récupérer les dimensions de l'écran
    height, width = screen.getmaxyx()

    # Calculer la position du message
    x = width // 2 - len("Quel est votre ID ?") // 2
    y = height // 2

    # Afficher le message
    screen.addstr(y, x, "Quel est votre ID ?")

    # Récupérer l'ID entré par l'utilisateur
    ID = screen.getstr(y+1, x)

    # Fermer la fenêtre
    curses.endwin()

    # Retourner l'âge sous forme de chaîne de caractères
    return ID.decode("utf-8")
