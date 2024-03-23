from utils.lines import *
import random
from menus.quiz import *


# Dados
def matematica():
    title = f"{b}Matemática{rt}"
    data = {
        f"{g}Cálculo Básico{rt}": calculoBasico,
        f"{b}Porcentagem{rt}": porcentagem,
        f"{y}Potência{rt}": potencia,
        # f"{r}Média{rt}": "media",
        # f"{m}Logaritmo{rt}": "logaritmo",
        # f"{m}Fatorial{rt}": "fatorial",
    }
    return title, data


# Assuntos
def porcentagem():
    title = f"{b}Porcentagem{rt}"
    texto = [
        f"{b}Porcentagem{rt} é uma forma de expressar uma parte de um todo em termos percentuais.\n\n{r}Macete{rt}: Para calcular a porcentagem de um valor, {r}multiplique o valor pela porcentagem{rt} e {g}mova a vírgula duas posições para a frente{rt}.\nPor exemplo, {r}20 alunos{rt},{g}35% são mulheres{rt}. 20 x 35 = 700.\nPortanto, 35% de 20 alunos são 7 alunas.",
        f"Para encontrar a {r}parte complementar{rt} (porcentagem restante),\nsubtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres,\n\n100% - 35% = 65% são homens.\n20 x 65 = 1300\n\nAssim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
        f"{r}Para encontrar o valor original{rt} de um numero com aumento em porcentagem.\n\n{r}[Valor com aumento]{g}/{r}(100+x%){rt}\n\nExemplo:\nSe um trabalhador tivesse {g}7% de aumento{rt} do seu {r}salario atual{rt} receberia {b}R$ 2.675,00{rt}.\n\n2675/(100+7)\n2675/107 = 2500\nValor do salario atual = 2500",
    ]

    q = quizp

    return (title, texto, q)


def quizp():
    # Gerar 2 valores
    x = random.randint(1, 101)
    y = random.randint(1, 101)

    resp = (x * y) / 100

    perg = f"Quanto é {r}{x}%{rt} de {g}{y}{rt} é?"

    return (perg, resp, "_")


# Calculos Basicos


def calculoBasico():
    title = f"{g}Cálculo Básico{rt}"
    texto = [
        f"{g}P: P{rt}arênteses (resolva as operações dentro dos {g}parênteses{rt} primeiro)\n{c}E: E{rt}xpoente (realize as operações com {c}expoentes{rt})\n{r}M: M{rt}ultiplicação (efetue as {r}multiplicações{rt})\n{r}D: D{rt}ivisão (faça as {r}divisões{rt})\n{m}A: A{rt}dição (realize as {m}adições{rt})\n{m}S: S{rt}ubtração (efetue as {m}subtrações){rt}\n",
        f"Macetes para Frações Decimais\nConverter para Fração: Coloque o número decimal sobre uma potência de 10 apropriada\n(por exemplo, 0,25 = 25/100 = 1/4)",
    ]
    q = quizmat

    return (title, texto, q)


def quizmat():
    # Gerar 2 valores
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

    resp = calcular(x, y, operador)
    perg = f"Quanto é {r}{x}{rt} {operador} {g}{y}{rt}?"
    return (perg, resp, "_")


def potencia():
    title = f"{g}Potência (Simples){rt}"
    texto = [
        f"{b}Potência{rt} é uma operação matemática que indica a multiplicação repetida de um número por si mesmo, um número específico de vezes. Ela é representada usando a notação de expoente, onde um número é elevado a uma certa potência.\n",
        f"{g}A operação de exponenciação por quadrados repetidos{rt} é uma técnica eficiente para calcular potências inteiras de um número. Ela consiste em decompor o expoente em sua representação binária e usar essa representação para realizar multiplicações sucessivas e quadrados do número base. Cada dígito binário do expoente representa uma potência de 2, e ao calcular os quadrados repetidos, é possível obter o resultado da potência de forma mais rápida do que com a multiplicação direta.\n",
        f"{y}Por exemplo, para calcular a^5{rt}, podemos decompor o expoente 5 em sua representação binária, que é 101. Então, ao realizar exponenciação por quadrados repetidos, começamos com a^1 = a, então a^2 = a * a, e a^4 = a^2 * a^2, e finalmente a^5 = a^4 * a. Esse método reduz o número de operações necessárias para calcular a potência, tornando-o mais eficiente.\n",
        f"{r}A exponenciação por quadrados repetidos{rt} é especialmente útil em computação e matemática aplicada, onde o desempenho e a eficiência são importantes. Ao aproveitar a estrutura binária do expoente, podemos calcular potências de forma mais rápida e eficiente, economizando tempo e recursos computacionais.\n",
        f"{m}Potências muito altas podem ser simplificadas da seguinte forma:{rt}\n"
        f"1.01^12 = ??\n"
        f"1.01^6 = 1.062\n"
        f"Logo:\n"
        f"(1.01^6)^2 = (1.062)^2\n"
        f"1.01^12 = 1.062*1.062\n"
        f"1.01^12 = 1.126724\n",
    ]

    q = quizpot

    return (title, texto, q)


def quizpot():
    x = round(random.uniform(1, 101))
    y = round(random.uniform(1, 5))

    resp = x**y

    perg = f"Quanto é {r}{x}{rt}^{g}{y}{rt}?"
    return (perg, resp, "_")
