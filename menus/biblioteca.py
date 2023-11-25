import os
from utils.lines import *
from menus.quiz import *


def QnE():
    x = input(f"{y}>> {rt}").upper()
    if x == "Q" or x == "1":
        return -1
    elif x == "E" or x == "2":
        return 1
    elif x == "R" or x == "3":
        return 3
    elif x == "0":
        return 2


def biblioteca(title, texto, quiz, r_correta):
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
            print(
                f"<< {len(texto)} | {m}{op+1}{rt} | {op+2} >>    0 - Voltar   3 - Quiz"
            )

        elif op == len(texto) - 1:
            print(f"<< {op} | {m}{op+1}{rt} | {1} >>   0 - Voltar   3 - Quiz")

        else:
            print(f"{op} | {m}{op+1}{rt} | {op+2} >>   0 - Voltar   3 - Quiz")

        o = QnE()

        if o == 3:
            os.system("cls")
            x = random.randint(0, 101)
            y = random.randint(0, 101)
            quiz_fun(title, quiz, x, y, r_correta)

        if o == 2:
            break

        op = op + o
        os.system("cls")


# biblioteca(*porcentagem())
