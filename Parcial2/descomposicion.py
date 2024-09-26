num = int(input("ingrese el numero: "))
n = 0
while num >= 1:
    n += num % 10 
    n = n * 10
    num = num // 10
print(n//10)