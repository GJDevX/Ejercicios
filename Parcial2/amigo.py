# Inicializa listas para almacenar tiempos de cada caminata
tiempos = []

# Ciclo para 4 meses
for mes in range(4):
    # Ciclo para 4 semanas en un mes
    for semana in range(4):
        # Ciclo para 3 días a la semana
        for dia in range(3):
            # Pide al usuario el tiempo invertido en esta caminata
            tiempo_invertido = float(input(f"Ingresa el tiempo invertido en la caminata {dia+1} de la semana {semana+1} del mes {mes+1}: "))
            # Agrega el tiempo a la lista
            tiempos.append(tiempo_invertido)

# Calcula el tiempo promedio por semana
tiempo_promedio_por_semana = sum(tiempos[:12]) / 12  # 3 caminatas/semana * 4 semanas

# Calcula el tiempo promedio por mes
tiempo_promedio_por_mes = sum(tiempos[:12]) / 4  # 12 caminatas/mes

# Calcula el tiempo promedio para 4 meses
tiempo_promedio_para_4_meses = sum(tiempos) / 48  # 48 caminatas en 4 meses

# Encuentra los tiempos mínimo y máximo
tiempo_minimo = min(tiempos)
tiempo_maximo = max(tiempos)

# Imprime los resultados
print("Tiempo promedio por semana:", tiempo_promedio_por_semana)
print("Tiempo promedio por mes:", tiempo_promedio_por_mes)
print("Tiempo promedio para 4 meses:", tiempo_promedio_para_4_meses)
print("Tiempo mínimo invertido:", tiempo_minimo)
print("Tiempo máximo invertido:", tiempo_maximo)