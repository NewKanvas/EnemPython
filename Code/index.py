import json
import os
import random
from time import sleep
from utils.lines import *

from quiz import quiz_fun
from interpretador import interp


# Carregar os dados do JSON
with open("LEARN-Prototype/Data/data.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

materias = list(dados.keys())


# Função para mostrar o menu
def mostrar_menu(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        # Verifica se é um dicionário
        if isinstance(opcao, dict):
            nome = list(opcao.keys())[0]  # Extrair o nome da categoria

        # Tratar como string caso não seja um dicionário
        else:
            nome = str(opcao)
        print(f"{i}. {nome}")


# Mostrando as materias
while True:
    os.system("cls")
    print(f"Escolha uma matéria:")
    mostrar_menu(materias)

    escolha = int(input(f"{y}>> {rt}"))

    if escolha == 0:
        print("Finalizando aplicação...")
        break
    elif escolha > len(materias) or escolha < 0:
        invalid()
        continue

    materia_escolhida = materias[escolha - 1]
    categorias = dados[materia_escolhida]

    # Mostrando as categorias
    while True:
        os.system("cls")
        # Printando titulo
        underline(materia_escolhida, "─", 4)
        overline(materia_escolhida, "─", 4)

        mostrar_menu(categorias)

        escolha = int(input(f"{y}>> {rt}"))

        if escolha == 0:
            break
        elif escolha > len(categorias) or escolha < 0:
            invalid()
            continue

        categoria_escolhida = categorias[escolha - 1]  # Selecionando a categoria

        # Procurar pela chave que contém uma lista de questões
        for key, value in categoria_escolhida.items():
            if isinstance(value, list):
                questoes = value
                break

        questao_aleatoria = random.choice(questoes)
        quiz_fun(*interp(questao_aleatoria))
