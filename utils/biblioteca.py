import os


def porcentagem():
    title = "Porcentagem"
    texto = [
        "Porcentagem é uma forma de expressar uma parte de um todo em termos percentuais.",
        "Macete: Para calcular a porcentagem de um valor, multiplique o valor pela porcentagem e mova a vírgula duas posições para a frente. Por exemplo, 20 alunos representam 35%. 20 x 35 = 700. Portanto, 35% de 20 alunos são 7 alunas.",
        "Para encontrar a parte complementar (porcentagem restante), subtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres, então 100% - 35% = 65% são homens. Para calcular a quantidade, multiplique a porcentagem complementar pelo valor total e mova a vírgula duas posições para a frente. Assim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
    ]

    return title, texto


def QnE():
    x = input(" >> ").upper()
    if x == "Q":
        return -1
    elif x == "E":
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

        header = " " * 4 + f"{title}" + " " * 4
        overline = "‾" * len(header)
        print(header, f"\n{overline}")

        print(texto[op], "\n")

        if op == 0:
            print(f"{len(texto)}<<{op+1}>>{op+2}")

        elif op == len(texto) - 1:
            print(f"{op}<<{op+1}>>{1}")

        else:
            print(f"{op}<<{op+1}>>{op+2}")

        x = QnE()

        if x == 2:
            break

        op = op + x
        os.system("cls")


# biblioteca(*porcentagem())
