from materias.matematica import *
from materias.portugues import *
from utils.lines import *


def materias():
    title = "Materias"
    lista = {
        f"{b}Matemática{rt}": matematica,
        f"{g}Português{rt}": portugues,
    }
    return title, lista
