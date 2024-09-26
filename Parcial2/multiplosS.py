num = int(input("ingrese un numero: "))

while num % 3 != 0:
    num += 1
num = num + 27

for i in range(1,11):
    print(num)
    num -= 3