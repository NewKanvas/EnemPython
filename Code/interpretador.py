import json
import random


# Carregar os dados do JSON (Teste)
with open("LEARN-Prototype/Data/data.json", "r") as file:
    dados = json.load(file)

data = random.choice(dados["Matematica"][0]["Calculo Basico"])


# Função do interpetrador
def interp(data):

    print("\n-------------------\n")
    print(data)
    print("\n-------------------\n")

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

    # Imprime os valores gerados
    for var, val in values.items():
        print(f"Valor de {var}: {val}")

    # Calculando resposta
    resposta = data["resposta"]  #
    for var, val in values.items():
        resposta = resposta.replace(var, str(val))
    resultado = eval(resposta)

    print(f"{resposta}\nResposta calculada: {resultado}")


interp(data)
