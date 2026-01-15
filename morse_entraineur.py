import tkinter as tk
import random

def play():
    # Dictionnaire des lettres et chiffres en morse
    morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '!': '-.-.--', '?': '..--..', ':': '---...', '/': '-..-.', ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', '=': '-...-', '-': '-....-', '_': '..--.-', "'": '.----.', '+': '.-.-.', '@': '.--.-.', '&': '.-...', '"': '.-..-.',' ':''}

    class MorseTrainer:
        def __init__(self, root):
            self.root = root
            self.root.title("Entraîneur de Morse")
            
            self.current_char = None  # Caractère actuel à deviner
            self.score = 0  # Score de l'utilisateur
            
            # Label pour afficher le code Morse
            self.morse_label = tk.Label(self.root, text="", font=("Arial", 24))
            self.morse_label.pack(pady=20)
            
            # Entry pour que l'utilisateur entre la lettre ou le chiffre
            self.entry = tk.Entry(self.root, font=("Arial", 24))
            self.entry.pack(pady=20)
            
            # Bouton pour vérifier la réponse
            self.check_button = tk.Button(self.root, text="Vérifier", font=("Arial", 16), command=self.check_answer)
            self.check_button.pack(pady=10)
            
            # Label pour afficher le score
            self.score_label = tk.Label(self.root, text=f"Score : {self.score}", font=("Arial", 16))
            self.score_label.pack(pady=10)
            
            # Bouton pour générer un nouveau code Morse
            self.next_button = tk.Button(self.root, text="Suivant", font=("Arial", 16), command=self.next_char)
            self.next_button.pack(pady=10)
            
            self.stop_button = tk.Button(self.root, text="Stop", font=('Arial',16), command=self.stop)
            self.stop_button.pack(pady=10)
            
            # Initialisation du jeu
            self.next_char()

        def stop(self):
            self.root.destroy()
        
        
        def next_char(self):
            """Générer un nouveau caractère et afficher son code Morse."""
            self.current_char = random.choice(list(morse_code.keys()))  # Choisir une lettre ou un chiffre au hasard
            morse = morse_code[self.current_char]  # Obtenir le code Morse
            self.morse_label.config(text=morse)  # Afficher le code Morse
            self.entry.delete(0, tk.END)  # Effacer l'Entry

        def check_answer(self):
            """Vérifier si la réponse de l'utilisateur est correcte."""
            user_input = self.entry.get().lower()  # Récupérer la réponse de l'utilisateur, en majuscule
            if user_input == self.current_char:
                self.score += 1
                self.score_label.config(text=f"Score : {self.score}")  # Mettre à jour le score
                self.next_char()  # Passer au prochain caractère
            else:
                self.morse_label.config(text=f"Incorrect, essayez encore!")  # Afficher un message d'erreur


    # Création de la fenêtre principale Tkinter
    root = tk.Tk()

    # Créer l'entraîneur de Morse
    trainer = MorseTrainer(root)

    # Lancer l'application Tkinter
    root.mainloop()
