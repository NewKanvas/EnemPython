import random
import os
from utils.lines import *


def quiz_fun(title, perguntas, x, y):
    q1 = random.choice(list(perguntas.keys()))

    r_correta = (x * y) / 100

    # Gere opções de resposta
    opcoes = [r_correta] + [
        ((x * y) / 100) + random.uniform(-0.5, 5) for _ in range(1, 4)
    ]

    random.shuffle(opcoes)

    overline(title, "─", 4)
    print(q1)
    underline(title, "─", 4)

    # Imprima as opções de resposta
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao:.2f}")

    resp = input(">> ")

    if int(resp) == opcoes.index(r_correta) + 1:
        print("\n✅ Correto")
        print(perguntas[q1])
        input(f"{y}Pressione Enter para continuar...{rt}")
        os.system("cls")

    else:
        print("\n❌ Incorreto")
        print(perguntas[q1])
        input(f"{y}Pressione Enter para continuar...{rt}")
        os.system("cls")
