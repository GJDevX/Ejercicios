import time

minutos = int(input("ingrese los minutos, no mayor a 60: "))
segundos = int(input("ingrese los segundos: "))
total_tiempo =  minutos * 60 + segundos 

if total_tiempo > 3600:
    print("el temporizador no puede exceder una hora.")
else:
    while total_tiempo > 0: 
        #divide los minutos por el tiempo total "div"
        #mod, es el residuo de una divicion.verifica que los segundos no pasen de lo estipulado "mod"
        #"divmod" hace estas dos funciones juntas
        minutos, segundos = divmod(total_tiempo, 60)
        print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
        # Esperar 1 segundo
        time.sleep(1)
        # Reducir el total de segundos
        total_tiempo -= 1
        # Mostrar mensaje de alerta cuando queden 5 minutos
        if total_tiempo== 5 * 60:
            print("\n¡Alerta! Faltan 5 minutos para que termine el tiempo.")
    
print("\nTiempo fuera.")