from materias.matematica import *
from materias.portugues import *
from materias.nocoesdedireito import *
from utils.lines import *


def materias():
    title = "Materias"
    data = {
        f"{b}Matemática{rt}": matematica,
        f"{g}Português{rt}": portugues,
        f"{y}Noções de Direito{rt}": nocoesdedireito,
    }
    return title, data
