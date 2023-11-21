from time import sleep
import os
import json


class Perfil:
    def __init__(self):
        self.arquivo_perfil = "perfil.json"
        self.maestria = self.load()

    def load(self):
        if os.path.exists(self.arquivo_perfil):
            with open(self.arquivo_perfil, "r") as arquivo:
                return json.load(arquivo)
        else:
            return {
                "Matematica": 0,
                "Portugues": 0,
                "Quimica": 0,
                "Biologia": 0,
                "Fisica": 0,
            }

    def save(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(dir, self.arquivo_perfil)

        with open(path, "w") as arquivo:
            json.dump(self.maestria, arquivo)

    def status(self):
        os.system("cls")
        print("=== Status do Perfil ===")
        for materia, maestria in self.maestria.items():
            print(f"{materia}: Maestria {maestria}%")
        input(f"Pressione Enter para continuar...")


user = Perfil()
user.save()  # Salva as alterações antes de sair
