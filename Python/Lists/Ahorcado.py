# -*- coding: utf-8 -*- 

import random

HANGMAN = ["""

    +---+
    |   |
        |
        |
        |
        |
        =========""", """

    +---+
    |   |
    O   |
        |
        |
        |
        =========""", """

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========""","""

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========""","""

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========""", """

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========""", """

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========""", """

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========""", """
"""]

WORDS=['escritorio','silla','mesa','cama','puerta','ventana','escalera','blanco','negro','gris','rojo','amarillo']

def choose_word():

    index = random.randint(0,len(WORDS)-1)
    return WORDS[index]


def display(hidden_word, tries):
    print(HANGMAN[tries])
    print("\n")
    print(hidden_word)
    print("===+++===+++===+++===++++===")
def start():
    word = choose_word()
    hidden_word=[' _ ']*len(word)
    tries = 0
    while True:
        display(hidden_word,tries)
        current_letter=str(input("Escoge una letra \n"))

        letter_indexes=[]
        for index in range(len(word)):
            letter_indexes.append(index)

        if len(letter_indexes)==0:
            tries+=1
        else:
            for index in letter_indexes:
                hidden_word[index]= current_letter    
            letter_indexes=[]

if __name__ == "__main__":
    print("Bienvenido al juego del ahorcado \n")
    start()