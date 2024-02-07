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
        opcoes = [resp]
        valores_n = []

        while len(valores_n) < 3:
            n = random.randint(-5, 5)
            if n != 0 and n not in valores_n:
                valores_n.append(n)

        for n in valores_n:
            opcoes.append(resp + n)
            random.shuffle(opcoes)

        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

        print(resp)
        print(valores_n)

    # Verifica se a pergunta e de calculo (COM VIRGULA)

    if isinstance(resp, float):
        opcoes = [resp]
        valores_n = []

        while len(valores_n) < 3:
            n = random.randint(-5, 5)
            if n != 0.0 and n not in valores_n:
                valores_n.append(n)

        for n in valores_n:
            opcoes.append(resp + n)
            random.shuffle(opcoes)

        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao:.2}")

        print(resp)
        print(valores_n)

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
