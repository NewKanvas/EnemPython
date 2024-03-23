import json
import os
from time import sleep
from utils.lines import *


# Carregar os dados do JSON
with open("LEARN-Prototype/Data/data.json", "r") as file:
    dados = json.load(file)

materias = list(dados.keys())


# Função para mostrar o menu
def mostrar_menu(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        # Verifica se é um dicionário
        if isinstance(opcao, dict):
            nome_categoria = list(opcao.keys())[0]  # Extrair o nome da categoria

        # Tratar como string caso não seja um dicionário
        else:
            nome_categoria = str(opcao)
        print(f"{i}. {nome_categoria}")


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
        print(materia_escolhida)

        mostrar_menu(categorias)

        escolha = int(input(f"{y}>> {rt}"))

        if escolha == 0:
            break
        elif escolha > len(categorias) or escolha < 0:
            invalid()
            continue

        categoria_escolhida = categorias[escolha - 1]
        # Aqui você pode fazer o que precisar com a categoria escolhida
        print(f"Categoria escolhida: {categoria_escolhida}")
        sleep(1)
