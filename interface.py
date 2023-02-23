import tkinter as tk

# création de la fenêtre principale
root = tk.Tk()
root.title("Ma première interface graphique")

# création d'un label
label = tk.Label(root, text="Hello World!")
label.pack()

# création d'un bouton qui quitte l'application
quit_button = tk.Button(root, text="Quitter", command=root.quit)
quit_button.pack()

# lancement de la boucle principale de l'application
root.mainloop()
