#solicita un numero base inicial.
valorm = int(input("Digita el valor minimo que quieres: "))
#solicita un numero de base final.
valor_M = int(input("Digita el valor maximo que quieres: "))
#solicita un valor que este entre lops dos rangos que acabaste de asignar 
intF = int(input("Ingresa un numero que este en el rango que acabaste de crear: "))
if valorm < intF and intF < valor_M:  
    #aqui determinamos los rangos requeridos 
    print ("Estas dentros de los intervalos. ")
else: 
    #si no pasamos de los rangos requeridos debemos indicarlo
    print ("No estas dentro de los intervalos ")