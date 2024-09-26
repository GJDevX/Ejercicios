print ("Bienvenido a la Universidad X, para iniciar con el proceso de matricula, debes pagar la misma. Tiene un valor de $1.000.000")
print ("Debes adicionar el seguro contra accidentes que tiene un valor de $200.000")

Pinicial = 1000000 #valor inicial de la matricula
Seguro = 200000    #valor del seguro
Credito = 350000   #valor de cada credito

num_creditos = float(input("Cuantos creditos deseas agregar? Cada uno cuesta $350.000 "))

total_c = num_creditos * Credito #se multiplica el numero de creditos agregados con su respectivo valor
total_apagar = total_c + Seguro + Pinicial #se suman el pago inicial con los creditos comprados para determinar el valor final

print ("Hola de nuevo! Su total a pagar es de: $", total_apagar)