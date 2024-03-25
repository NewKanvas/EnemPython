from time import sleep
import os

r = "\033[91m"  # Vermelho
g = "\033[92m"  # Verde
y = "\033[93m"  # Amarelo
b = "\033[94m"  # Azul
m = "\033[95m"  # Magenta
c = "\033[96m"  # Ciano
w = "\033[97m"  # Branco
rt = "\033[0m"  # Resetar cor


def overline(title, symbol, size):
    header = " " * size + f"{title}" + " " * size
    overline = symbol * len(header)

    print(header, f"\n{overline}")


def underline(title, symbol, size):
    header = " " * size + f"{title}" + " " * size
    overline = symbol * len(header)

    print(f"{overline}")


def invalid():
    print(f"{r}Escolha inválida.{rt}")
    sleep(1)
    os.system("cls")
