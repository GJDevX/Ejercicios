Intervalo1 = int(input("Escribe el primer intervalo:"))
Intervalo2 = int(input("Escribe el segundo intervalo "))
intervalos = Intervalo1 
simpar = 0
spar = 0

for intervalos in range(Intervalo1, Intervalo2+1):
    if intervalos % 2 == 0:
        spar = spar + intervalos 
    else:
        simpar = simpar + intervalos
print (f"la sumatoria de numeros pares es {spar} y la sumatoria de numeros impares es {simpar}")