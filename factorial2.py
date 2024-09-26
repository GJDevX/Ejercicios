factorial = int(input("Ingrese el numero para calcular factorial: "))
contador = 1
total = 1
for i in range(1, factorial+1):
    total = total * contador
    contador = contador + 1 
    print(f"el factorial de {factorial} es {contador}")