import random
import os

User_Letters = []
Chosen_Word = []
Words = []


def run():

    with open("./Archivos/data.txt", "r") as data:
        for i in data:
            Words.append(i.strip().upper())

    Chosen_Word = list(random.choice(Words))
    User_Letters = ["-" for i in range(0, len(Chosen_Word))]

    while Chosen_Word != User_Letters:

        os.system("clear")
        print("Adivina la palabra: ")
        print(''.join(User_Letters))

        New_Input = input("Prueba con una letra: ").upper()

        for i in range(0, len(Chosen_Word)):
            if Chosen_Word[i] == New_Input:
                User_Letters[i] = New_Input

    os.system("clear")
    print("Felicidades has ganado, La palabra era: ")
    print(''.join(Chosen_Word))


if __name__ == '__main__':
    run()