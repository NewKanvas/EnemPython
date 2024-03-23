import json
import random


# Carregar os dados do JSON
with open("LEARN-Prototype/Data/data.json", "r") as file:
    data = json.load(file)

print("\n-------------------\n")
print(data)
print("\n-------------------\n")

x_range = list(map(int, data["x"].split(",")))
y_range = list(map(int, data["y"].split(",")))

x = random.randint(x_range[0], x_range[1] + 1)

print(x)
