from time import sleep
import os

r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
b = "\033[94m"
m = "\033[95m"
c = "\033[96m"
w = "\033[97m"
rt = "\033[0m"


def overline(title, symbol, size):
    header = " " * size + f"{title}" + " " * size
    overline = symbol * len(header)

    print(header, f"\n{overline}")


def underline(title, symbol, size):
    header = " " * size + f"{title}" + " " * size
    overline = symbol * len(header)

    print(f"{overline}")


def invalid():
    print(f"{r}Invalid Option{rt}")
    sleep(1)
    os.system("cls")
