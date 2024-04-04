import json
import random
import os  # Debug
import re
from utils.lines import *
from quiz import quiz_fun

"""
# Carregar os dados do JSON (Teste)
with open("LEARN-Prototype/Data/data.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

categoria_mate = dados["Português"][1]
pergunta_aleatoria = random.choice(
    categoria_mate[next(iter(categoria_mate))]["perguntas"]
)

print(pergunta_aleatoria)
"""


# Função do interpetrador
def interp(data, dataAcima):
    # os.system("cls")
    # print(data)  # (Debug)
    print("\n\n")

    if "variaveis" in data:
        variaveis = data["variaveis"]
        values = {}

        for var, var_range in variaveis.items():
            if "." in var_range:
                var_range = list(map(float, var_range.split(",")))
                values[var] = round(random.uniform(var_range[0], var_range[1]), 2)
            else:
                var_range = list(map(int, var_range.split(",")))
                values[var] = random.randint(var_range[0], var_range[1])

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

        return (pergunta, resultado, "_")

    elif "falsa" in data:
        pergunta = data["pergunta"]
        resposta = data["resposta"]
        falsas = data["falsa"]

        # print(f"{r}Pergunta:{rt} {pergunta}",f"{r}Repostas:{rt} {resposta}",f"{r}Falsas:{rt} {falsas}",)

        if len(falsas) < 3:
            banco_falsas = dataAcima["falsas"]
            falsas = falsas + banco_falsas
            pass

        return (pergunta, resposta, falsas)


# quiz_fun(*interp(pergunta_aleatoria))
# quiz_fun(perg, resp, falsas)

# print(interp(pergunta_aleatoria))
