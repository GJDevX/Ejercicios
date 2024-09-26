num = int(input("Ingrese un numero: "))
x = 1
while num > 50:
    num = int(input("Ingrese un numero: "))
for factorial in range(1, num+1):
    x *= factorial
print (x)