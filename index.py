from time import sleep
import os
from utils.biblioteca import *
from utils.cores import *
from materias.materias import *


def tuto():
    os.system("cls")

    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)

    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")

    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


def menu2(title, lista):
    while True:
        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)

        print(header, f"\n{overline}")

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        x = int(input("\n>> ")) - 1

        if x in range(len(lista)):
            biblioteca(*lista[list(lista.keys())[x]]())
            os.system("cls")

        else:
            print("Invalid Option")
        os.system("cls")


def menu(title, lista):
    while True:
        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)

        print(header, f"\n{overline}")

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        x = int(input("\n>> ")) - 1

        if x in range(len(lista)):
            menu2(*lista[list(lista.keys())[x]]())
            os.system("cls")

        else:
            print("Invalid Option")
        os.system("cls")


# tuto()
menu(*materias())
