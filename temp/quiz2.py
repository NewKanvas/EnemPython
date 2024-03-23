import random
import os

# Cores
r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
b = "\033[94m"
m = "\033[95m"
c = "\033[96m"
w = "\033[97m"
rt = "\033[0m"


# Gerando perguntas


def quiztext2():
    perguntas = {
        "pergunta A": {"respcorretaA": ["resp1A", "resp2A", "resp3A"]},
        "pergunta B": {"respcorretaB": ["resp1B", "resp2B", "resp3B"]},
        "pergunta C": {"respcorretaC": ["resp1C", "resp2C", "resp3C"]},
        "pergunta D": {"respcorretaD": ["resp1D", "resp2D", "resp3D"]},
    }

    perg3 = random.choice(list(perguntas.keys()))
    resp3 = list(perguntas[perg3].keys())[0]
    falsas3 = perguntas[perg3][resp3]

    return (perg3, resp3, falsas3)


# Pergunta Calculo Basico


# Gerar 2 valores
def quizmat():
    x = round(random.uniform(1, 101))
    y = round(random.uniform(1, 101))

    # Gera o tipo de calculo
    operadores = ["+", "-", "*", "/"]
    operador = random.choice(operadores)

    def calcular(x, y, operador):
        if operador == "+":
            resp = x + y
        elif operador == "-":
            resp = x - y
        elif operador == "*":
            resp = x * y
        elif operador == "/":
            resp = x / y

        return resp

    resp2 = calcular(x, y, operador)
    perg2 = f"Quanto é {r}{x}{rt} {operador} {g}{y}{rt}?"
    return (perg2, resp2, "_")


def quiztext2():
    perguntas = {
        "pergunta A": {"respcorretaA": ["resp1A", "resp2A", "resp3A"]},
        "pergunta B": {"respcorretaB": ["resp1B", "resp2B", "resp3B"]},
        "pergunta C": {"respcorretaC": ["resp1C", "resp2C", "resp3C"]},
        "pergunta D": {"respcorretaD": ["resp1D", "resp2D", "resp3D"]},
    }

    perg3 = random.choice(list(perguntas.keys()))
    resp3 = list(perguntas[perg3].keys())[0]
    falsas3 = perguntas[perg3][resp3]

    return (perg3, resp3, falsas3)


# Função


def quiz(perg, resp, falsas):
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


# Teste texto
# quiz(*quiztext())

# Teste texto Multiplos
while True:
    quiz(*quiztext2())

# Teste Calculo
# quiz(*quizmat())
