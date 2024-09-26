import numpy as np
numeros = np.random.randint(1, 100, size=500)

nmayor = 0
nmenor = 0

for poblacion in (numeros):
    if poblacion > 18:
        nmayor += 1
    else:
        nmenor += 1
print(numeros)
print(f"{nmayor} son personas mayores de edad")
print(f"{nmenor} son personas menores de edad.")
