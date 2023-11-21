import random

# from utils.cores import *


def gerarP():
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    # Crie a listaP apenas com o formato das perguntas, sem valores específicos
    listaP = {
        f"{x}% de {y} é?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {((x*y)/100):.2f}",
        f"{x} é quanto de {y}%?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {((x*y)/100):.2f}",
    }

    q1 = random.choice(list(listaP.keys()))

    r_correta = x * y / 100

    # Gere opções de resposta
    opcoes = [r_correta] + [((x * y) / 100) + random.randint(1, 6) for _ in range(1, 4)]

    random.shuffle(opcoes)

    print(q1)

    # Imprima as opções de resposta
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao:.2f}")

    resp = input(">> ")

    if int(resp) == opcoes.index(r_correta) + 1:
        print("✅ Correto")
        print(listaP[q1])

    else:
        print("❌ Incorreto")
        print(listaP[q1])


gerarP()
