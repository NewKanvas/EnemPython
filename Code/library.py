import json
import random
from utils.lines import *
from quiz import quiz_fun
from interpretador import interp
import os  # Debug


def categoria_tem_texto(categoria):
    if isinstance(categoria, dict) and "texto" in categoria:
        return True
    return False


def QnE():
    x = input(">> ").upper()
    if x == "Q" or x == "1":
        return -1

    elif x == "E" or x == "2":
        return 1

    elif x == "R" or x == "3":  # iniciar quiz
        return 0

    elif x == "0":
        return 2


""
# Carregar os dados do JSON (Teste)
with open("LEARN-Prototype/Data/data.json", "r", encoding="utf-8") as file:
    dados = json.load(file)
""


port = dados["Português"][0]["Gramática Básica"]
mat = dados["Matemática"][0]["Calculo Basico"]
mat2 = dados["Matemática"][2]["Porcentagem"]

# print(mat)

"""
print(categoria_tem_texto(port))  # True
print(categoria_tem_texto(mat))  # True
print(categoria_tem_texto(mat2))  # False
"""


def library(data):
    os.system("cls")
    index = 0
    title = "Texto"
    text = "\n".join(data["texto"])

    # Verifica se há perguntas disponíveis
    if "perguntas" in data:
        has_questions = True
    else:
        has_questions = False

    while True:
        if index < 0:
            index = len(data["texto"]) - 1
        elif index >= len(data["texto"]):
            index = 0

        overline(title, "─", 4)
        print(text[index:])
        underline(title, "─", 4)

        if index == 0:
            if has_questions:
                print(
                    f"<< {len(data['texto'])} | {m}{index+1}{rt} | {index+2} >>    0 - Voltar   3 - Quiz"
                )
            else:
                print(
                    f"<< {len(data['texto'])} | {m}{index+1}{rt} | {index+2} >>    0 - Voltar"
                )

        elif index == len(data["texto"]) - 1:
            if has_questions:
                print(f"<< {index} | {m}{index+1}{rt} | {1} >>   0 - Voltar   3 - Quiz")
            else:
                print(f"<< {index} | {m}{index+1}{rt} | {1} >>   0 - Voltar")

        else:
            if has_questions:
                print(
                    f"{index} | {m}{index+1}{rt} | {index+2} >>   0 - Voltar   3 - Quiz"
                )
            else:
                print(f"{index} | {m}{index+1}{rt} | {index+2} >>   0 - Voltar")

        o = QnE()

        if o == 2:
            break

        if o == 0 and has_questions:
            pergunta = random.choice(data["perguntas"])
            quiz_fun(*interp(pergunta))
            pass

        index = index + o
        os.system("cls")


# library(port)
