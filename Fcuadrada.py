a = int(input("Escribe el valor de a: "))
b = int(input("Escribe el valor de b: "))
c = int(input("Escribe el valor de c: "))

if a != 0 and ((b*b)-(4*a*c)) >= 0:
    print ("Tienen solución.")
else:
    print ("No tienen solución.")
