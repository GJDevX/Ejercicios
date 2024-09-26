num = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
total = 0
while num < 0 or num2 < 0:
    print ("incorrecto, uno de los dos numeros es negativo")
    num = int(input("ingresa el primer numero: "))
    num2 = int(input("ingresa el segundo numero: "))
    total = num + num2 
    print ("la suma es: ", total)