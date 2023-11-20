from time import sleep

# Biblioteca


def matematica():
    title = "Matematica"
    lista = {
        "Porcentagem": porcentagem,
        "Media": media,
        "Logaritimo": logaritimo,
    }
    return title, lista


# Assuntos


def porcentagem():
    title = "Porcentagem"
    texto = [
        "Porcentagem é uma forma de expressar uma parte de um todo em termos percentuais.",
        "Macete: Para calcular a porcentagem de um valor, multiplique o valor pela porcentagem e mova a vírgula duas posições para a frente. Por exemplo, 20 alunos representam 35%. 20 x 35 = 700. Portanto, 35% de 20 alunos são 7 alunas.",
        "Para encontrar a parte complementar (porcentagem restante), subtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres, então 100% - 35% = 65% são homens. Para calcular a quantidade, multiplique a porcentagem complementar pelo valor total e mova a vírgula duas posições para a frente. Assim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
    ]

    return title, texto


def logaritimo():
    lista = [
        "Logaritimo e pika",
        "Multiplica os 2 e joga a virgula duas vezes para frente",
    ]

    print(lista[0])


def media():
    lista = [
        "Media e pika",
        "Multiplica os 2 e joga a virgula duas vezes para frente",
    ]

    print(lista[0])
