frase = input("ingrese una frase: ")
contador_c = 0

for caracter in range(0,len(frase)+1):
    if caracter != " ":
        contador_c = caracter +  1

print(f" la frase {frase} tiene {contador_c} caracteres.")