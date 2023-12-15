import random
import os
from utils.lines import *



def quiz_fun(title, quiz, x, y, r_correta):
    q1 = random.choice(list(quiz.keys()))

    # Gere opções de resposta
    opcoes = [r_correta] + [r_correta + random.uniform(-0.5, 5) for _ in range(1, 4)]

    random.shuffle(opcoes)

    overline(title, "─", 4)
    print(q1)
    underline(title, "─", 4)

    # Imprima as opções de resposta
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao:.2f}")

    resp = input(">> ")

    if int(resp) == opcoes.index(r_correta) + 1:
        print("\n✅ Correto")
        print(quiz[q1])
        input(f"{y}Pressione Enter para continuar...{rt}")
        os.system("cls")

    else:
        print("\n❌ Incorreto")
        print(quiz[q1])
        input(f"{y}Pressione Enter para continuar...{rt}")
        os.system("cls")
