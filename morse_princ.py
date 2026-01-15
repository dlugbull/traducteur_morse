import tkinter as tk

def traducteur():
    # Créer une nouvelle fenêtre
    import morse_trad
    morse_trad.play()

def entraineur():
    import morse_entraineur
    morse_entraineur.play()

# Fenêtre principale
root = tk.Tk()
root.title("Morse")
root.geometry("250x100")

# Ajouter un bouton pour ouvrir une nouvelle fenêtre
button = tk.Button(root, text="Traduire du texte",font=("Arial", 16), command=traducteur)
button.pack()

button1 = tk.Button(root, text="Entraîneur",font=("Arial", 16), command= entraineur)
button1.pack()

# Lancer l'application
root.mainloop()
