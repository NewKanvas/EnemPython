import os
from utils.lines import *
from utils.cores import *


def QnE():
    x = input(f"{y}>> {rt}").upper()
    if x == "Q" or x == "1":
        return -1
    elif x == "E" or x == "2":
        return 1
    elif x == "0":
        return 2


def biblioteca(title, texto):
    op = 0

    while True:
        if op < 0:
            op = len(texto) - 1
        elif op >= len(texto):
            op = 0

        overline(title, "─", 4)
        print(texto[op], "\n")
        underline(title, "─", 4)

        if op == 0:
            print(f"<< {len(texto)} | {m}{op+1}{rt} | {op+2} >>    0 - Voltar")

        elif op == len(texto) - 1:
            print(f"<< {op} | {m}{op+1}{rt} | {1} >>   0 - Voltar")

        else:
            print(f"{op} | {m}{op+1}{rt} | {op+2} >>   0 - Voltar")

        x = QnE()

        if x == 2:
            break

        op = op + x
        os.system("cls")


# biblioteca(*porcentagem())
