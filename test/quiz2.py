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


# Perguta texto
def quiztext():
    perg1 = "pergunta 1"
    resp1 = "respcorreta"
    falsas1 = [
        "resp1",
        "resp2",
        "resp3",
        "resp4",
        "resp5",
        "resp6",
        "resp7",
        "resp8",
    ]
    return (perg1, resp1, falsas1)


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


# Teste texto
quiz(*quiztext())

# Teste Calculo
quiz(*quizmat())
