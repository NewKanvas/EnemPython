from time import sleep
import os
from utils.biblioteca import *
from utils.cores import *
from materias.materias import *
from utils.lines import *


def tuto():
    os.system("cls")
    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)
    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")
    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


def invalid():
    print(f"{r}Invalid Option{rt}")
    sleep(1)
    os.system("cls")


def submenu(title, lista):
    while True:
        os.system("cls")
        overline(title, "─", 4)

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        underline(title, "─", 4)
        print("\n0 - Voltar")

        x = int(input(f"{y}>> {rt}")) - 1

        if x == -1:
            break

        if x in range(len(lista)):
            os.system("cls")
            biblioteca(*lista[list(lista.keys())[x]]())

        else:
            invalid()


def menu(title, lista):
    while True:
        os.system("cls")
        overline(title, "─", 4)

        for i, op in enumerate(lista):
            print(f"{i+1} - {op}")

        underline(title, "─", 4)
        print("\n0 - Voltar")

        x = int(input(f"{y}>> {rt}")) - 1

        if x == -1:
            print("Saindo...")
            sleep(1)
            os.system("cls")
            break

        if x in range(len(lista)):
            os.system("cls")
            submenu(*lista[list(lista.keys())[x]]())

        else:
            invalid()


# tuto()
menu(*materias())
