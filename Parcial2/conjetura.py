num = int(input("Ingrese el numero: "))

while num > 1:
    if num % 2 == 0:
        num = num // 2 
        print (num, ",", end=" ")
    else: 
        num = num * 3 + 1
        print(num, ",", end=" ")