import json
import random
import os  # Debug
import re
from utils.lines import *
from quiz import quiz_fun


"""# Carregar os dados do JSON (Teste)
with open("LEARN-Prototype/Data/data.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

data = random.choice(dados["Matematica"][0]["Calculo Basico"])
"""


# Função do interpetrador
def interp(data):
    os.system("cls")
    # print(data)  # (Debug)
    print("\n\n")

    # Gerando valores para variaveis
    variaveis = data["variaveis"]
    values = {}

    for var, var_range in variaveis.items():  # pega cada variaveis e seu "valor"
        var_range = list(
            map(int, var_range.split(","))
        )  # separa os parametros das variaveis
        values[var] = random.randint(
            var_range[0], var_range[1]
        )  # gera um valor para cada variavel

    # Imprime os valores gerados (Debug)
    # for var, val in values.items():
    #    print(f"Valor de {var}: {val}")

    # Calculando resposta
    resposta = data["resposta"]
    for var, val in values.items():
        resposta = resposta.replace(var, str(val))
    resultado = eval(resposta)  # Gerando resultado com base na resposta

    # Definindo sequencia de cores:
    # colors = [r, b, g, y, c, m]

    # Formantado pergunta
    pergunta = data["pergunta"]
    for var, val in values.items():
        pergunta = re.sub(
            rf"\b{re.escape(var)}\b", str(val), pergunta
        )  # Pegando a variavel separada por espaços

        # Gerando cor aleatoria para os valores
        pergunta = pergunta.replace(
            str(val), f"\033[{random.randint(91, 96)}m {str(val)} \033[0m"
        )

    # print(pergunta)  # Debug
    # print(f"Resposta calculada: {resultado}")  # Debug

    return (pergunta, resultado, "_")


# quiz_fun(*interp(data))
