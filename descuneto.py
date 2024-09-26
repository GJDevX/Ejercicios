descuento = 0.15
costo = float(input("ingresa el valor del producto que quieres comprar. "))

if costo > 150000:

    print ("aplicas para un descuento de 5%. ")
    articulo_descuento = costo * descuento
    descuento = costo - articulo_descuento
    
    print ("el valor a pagar es: ", descuento)
    
else: 
    print ("no aplicas para un descuento. ")
