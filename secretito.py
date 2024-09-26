numero_secreto = 7
numero = int(input("Adivina el número entre 1 y 10: "))

while numero != numero_secreto:
    print("Incorrecto, intenta de nuevo")
    numero = int(input("Adivina el número entre 1 y 10: "))

print("¡Correcto!")
