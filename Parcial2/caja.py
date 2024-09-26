menu = int(9999)
base = int()
ingresos = int()
egresos = int()
total = 0

while menu != 0:
    menu= int(input("1. Agregar la base del día: \n2. Agregar los ingresos: \n3. Agregar egresos: \n0. Salir.\n"))
    
    if menu == 1:
        base = int(input("Cual es la base: "))
        print("La base es: ", base)
        total += base
    
    elif menu == 2:
        ingresos = int(input("Cuales son los ingresos: "))
        total += ingresos
        print("los ingresos son: ", total)
    
    elif menu == 3:
        egresos = int(input("Cuales son los egresos: "))
        total -= egresos
        print("Estos son los egresos", egresos)
        
    if total < base * 0.15:
        print("revisa bien los calculos, estas por debajo de los niveles desados.")

print(f"La base es {base}, los ingresos son {ingresos} y estos son los egresos {egresos}\npara un total de {total}")
