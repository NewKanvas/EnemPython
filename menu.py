from time import sleep
import os
from biblioteca import *
from cores import *
from matematica import *


def tuto():
    os.system("cls")

    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)

    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")

    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


title = "Matematica"
lista = {
    "Porcentagem": porcentagem,
    "Media": media,
    "Logaritimo": logaritimo,
    "Geometria": geometria,
    "Equações Lineares": equacoes_lineares,
    "Trigonometria": trigonometria,
}


def menu(title, lista):
    while True:
        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)

        print(header, f"\n{overline}")

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        x = int(input(" >> ")) - 1

        if x in range(len(lista)):
            biblioteca(*lista[list(lista.keys())[x]]())

        else:
            print("Invalid Option")
        os.system("cls")


# tuto()
menu(title, lista)
