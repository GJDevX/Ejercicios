factorial = int(input("Ingresa el numero: "))
Auxilar = 1
total = 1
if factorial > 0:
    while Auxilar <= factorial:
        total =  total * Auxilar
        Auxilar = Auxilar + 1
print ("El factorial de tu número es: ", total)