from random import*
import tkinter as tk
from tkinter import ttk
def play():
    carac_diff="abcdefghijklmnopqrstuvwxyz0123456789,.!?:/;()=-_'+@&"+'"'
    a_m={'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '!': '-.-.--', '?': '..--..', ':': '---...', '/': '-..-.', ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', '=': '-...-', '-': '-....-', '_': '..--.-', "'": '.----.', '+': '.-.-.', '@': '.--.-.', '&': '.-...', '"': '.-..-.',' ':''}

    m_a = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x','-.--':'y' ,'--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '--..--': ',', '.-.-.-': '.', '-.-.--': '!', '..--..': '?', '---...': ':', '-..-.': '/', '-.-.-.': ';', '-.--.': '(', '-.--.-': ')', '-...-': '=', '-....-': '-', '..--.-': '_', '.----.': "'", '.-.-.': '+', '.--.-.': '@', '.-...': '&', '.-..-.': '"', '':' '}

    def morse_texte(msg):
        msgfin=''
        msg=msg.split('/')
        for i in msg:
            msgfin+=m_a[i]
        return msgfin

    def texte_morse(msg):
        msg=msg.lower()
        msgfin=''
        for i in msg:
            msgfin+=a_m[i]+'/'
        msgfin=msgfin[:len(msgfin)-1]
        return msgfin

    fen=tk.Tk()
    fen.title('Traducteur morse/texte')
    fen.geometry('600x500')

    #frame1
    frame1 = tk.Frame(fen)
    frame1.pack(pady=10, fill=tk.X)

    # Liste déroulante dans la première frame
    label1 = tk.Label(frame1, text="Language à traduire ?",font=("Arial", 16))
    label1.pack()

    options1 = ["Morse", "Texte"]
    menu1 = ttk.Combobox(frame1, values=options1,font=("Arial", 16))
    menu1.pack(pady=5)

    # Zone de texte dans la première frame
    zone_texte1 = tk.Text(frame1, height=5, width=30,font=("Arial", 16))
    zone_texte1.pack(pady=5, fill=tk.X)

    # Frame 2
    frame2 = tk.Frame(fen)
    frame2.pack(pady=10, fill=tk.X)


    # Zone de texte dans la deuxième frame
    zone_texte2 = tk.Label(frame2, height=5, width=30,font=("Arial", 24))
    zone_texte2.pack(pady=5, fill=tk.X)

    def traduire():
        language=menu1.get()
        msg = zone_texte1.get("1.0", tk.END).strip()
        if language == 'Morse' :
            msgfin = morse_texte(msg)
        elif language == 'Texte':
            msgfin = texte_morse(msg)
        else :
            msgfin = 'Veulliez choisir une option de traduction.'
        zone_texte2.config(text=msgfin)

    bouton = tk.Button(fen, text="Traduire",font=("Arial", 16), command=traduire)
    bouton.pack(pady=10)
        
    fen.mainloop()
