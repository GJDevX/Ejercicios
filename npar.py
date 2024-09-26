npar = int(input("Ingrese cualesquier número: "))
contp = 0
totalp = 0
while contp < npar:
    if contp % 2 == 0:
        totalp = totalp + 1
    contp = contp + 1
print ("La cantidad de pares es: ", totalp)