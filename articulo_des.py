numero = int(input("Ingresa un número: "))
contador = 0
i = 1

while i <= numero:
    if i % 2 == 0:
        contador += 1
    i += 1

print("Cantidad de números pares:", contador)

