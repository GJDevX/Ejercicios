num1 = 6
num2 = int(input("ingrese un numero: "))

while num2 < 6:
    num2 = int(input("ingrese un numero: "))

for multiplos in range(num1, num2+1):
    if multiplos % 3 == 0:
        print("el resultado es: ", multiplos)