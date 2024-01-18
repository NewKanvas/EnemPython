import random
import os
from utils.lines import *


def quiz_fun(perg, resp, falsas):
    print(perg)

    # Verifica se a pergunta e de texto
    if isinstance(resp, str):
        opcoes = [resp] + random.sample(falsas, 3)
        random.shuffle(opcoes)

        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

    # Verifica se a pergunta e de calculo (INTEIRO)

    if isinstance(resp, int):
        opcoes = [resp] + [resp + random.randint(-5, 5) for _ in range(1, 4)]
        random.shuffle(opcoes)

        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

    # Verifica se a pergunta e de calculo (COM VIRGULA)

    if isinstance(resp, float):
        opcoes = [resp] + [resp + random.uniform(-5, 5) for _ in range(1, 4)]
        random.shuffle(opcoes)

        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao:.2f}")

    # Corretor
    op = input(">> ")

    if int(op) == opcoes.index(resp) + 1:
        print("\n✅ Correto")
        print(f"Resposta correta é:\n{resp}")
        input(f"{g}Pressione Enter para continuar...{rt}")
        os.system("cls")

    else:
        print("\n❌ Incorreto")
        print(f"Resposta correta é:\n{resp}")
        input(f"{r}Pressione Enter para continuar...{rt}")
        os.system("cls")
