import random
import os
from utils.lines import *
import time


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

    # Repondendo

    start_time = time.time()  # Registra o tempo antes da resposta

    op = input(">> ")

    end_time = time.time()  # Registra o tempo depois da resposta
    response_time_seconds = (
        end_time - start_time
    )  # Calcula o tempo de resposta em segundos
    response_time_minutes = response_time_seconds / 60  # Converte para minutos

    print(f"Tempo de resposta: {response_time_minutes:.2f} minutos")
    print(f"Tempo médio por pergunta no ENEM tem de ser 2 minutos e 30 segundos")

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
