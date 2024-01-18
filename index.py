from time import sleep
import os
from menus.biblioteca import *
from materias.materias import *

from utils.lines import *


# Mecanismo de filtragem de resposta do menu
def QnE():
    x = input(f"{y}>> {rt}").upper()
    if x == "Q":
        return -1
    elif x == "E" or x == "2":
        return 1
    elif x == "0":
        return 2


# Mesagem de tutorial
def tuto():
    os.system("cls")
    print("Bem-vindo ao meu mapa mental de estudo.\n")
    sleep(1)
    print("'E' para avançar;")
    print("'Q' para retornar;")
    print("'0' para sair.\n")
    input(f"{y}Pressione Enter para continuar...{rt}")
    os.system("cls")


def submenu(title, data):
    while True:
        os.system("cls")
        overline(title, "─", 4)  #

        for i, op in enumerate(data):
            print(f"{i+1} - {op}")

        underline(title, "─", 4)
        print("\n0 - Voltar")

        x = int(input(f"{y}>> {rt}")) - 1

        if x == -1:
            break

        if x in range(len(data)):
            os.system("cls")
            biblioteca(*data[list(data.keys())[x]]())

        else:
            invalid()


def menu(title, data):
    while True:
        os.system("cls")
        overline(title, "─", 4)

        for i, op in enumerate(data):
            print(f"{i+1} - {op}")

        underline(title, "─", 4)
        print("\n0 - Sair")

        x = int(input(f"{y}>> {rt}")) - 1

        if x == -1:
            print("Saindo...")
            sleep(1)
            os.system("cls")
            break

        if x in range(len(data)):
            os.system("cls")
            submenu(*data[list(data.keys())[x]]())

        else:
            invalid()


# tuto()
menu(*materias())
