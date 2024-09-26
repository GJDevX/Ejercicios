import turtle

# Configurar la ventana
ventana = turtle.Screen()
ventana.title("Carrera de Buses Interactiva")
ventana.bgcolor("lightgray")
ventana.setup(width=800, height=600)

# Crear la línea de meta
meta = turtle.Turtle()
meta.penup()
meta.goto(300, 250)
meta.pendown()
meta.right(90)
meta.forward(500)
meta.hideturtle()

# Crear el bus del jugador 1 (Rojo)
bus1 = turtle.Turtle()
bus1.color("red")
bus1.shape("square")
bus1.shapesize(stretch_wid=1.5, stretch_len=3)
bus1.penup()
bus1.goto(-300, 100)

# Crear el bus del jugador 2 (Azul)
bus2 = turtle.Turtle()
bus2.color("blue")
bus2.shape("square")
bus2.shapesize(stretch_wid=1.5, stretch_len=3)
bus2.penup()
bus2.goto(-300, -100)

# Variable para verificar si la carrera ha terminado
carrera_terminada = False

# Mostrar un mensaje en pantalla
def mostrar_mensaje(texto, tamaño):
    mensaje = turtle.Turtle()
    mensaje.hideturtle()
    mensaje.penup()
    mensaje.goto(0, 200)
    mensaje.write(texto, align="center", font=("Arial", tamaño, "bold"))

# Funciones para mover los buses
def mover_bus1():
    global carrera_terminada
    if not carrera_terminada and bus1.xcor() < 300:
        bus1.forward(10)  # Avanza el bus 1
    verificar_ganador()

def mover_bus2():
    global carrera_terminada
    if not carrera_terminada and bus2.xcor() < 300:
        bus2.forward(10)  # Avanza el bus 2
    verificar_ganador()

# Función para verificar si hay un ganador
def verificar_ganador():
    global carrera_terminada
    if bus1.xcor() >= 300:
        mostrar_mensaje("¡El Bus Rojo Gana!", 24)
        carrera_terminada = True
    elif bus2.xcor() >= 300:
        mostrar_mensaje("¡El Bus Azul Gana!", 24)
        carrera_terminada = True

# Función para reiniciar la carrera
def reiniciar_carrera():
    global carrera_terminada
    bus1.goto(-300, 100)
    bus2.goto(-300, -100)
    carrera_terminada = False
    ventana.clear()  # Limpiar la pantalla
    ventana.title("Carrera de Buses Interactiva")
    ventana.bgcolor("lightgray")
    ventana.setup(width=800, height=600)
    meta.penup()
    meta.goto(300, 250)
    meta.pendown()
    meta.right(90)
    meta.forward(500)
    meta.hideturtle()
    mostrar_mensaje("Presiona 'Enter' para empezar la carrera", 18)

# Iniciar la carrera al presionar 'Enter'
def empezar_carrera():
    ventana.onkey(mover_bus1, "a")  # Jugador 1 mueve el bus con la tecla "a"
    ventana.onkey(mover_bus2, "l")  # Jugador 2 mueve el bus con la tecla "l"
    ventana.listen()

# Función principal
def main():
    mostrar_mensaje("Presiona 'Enter' para empezar la carrera", 18)
    ventana.listen()
    ventana.onkey(empezar_carrera, "Return")
    ventana.onkey(reiniciar_carrera, "r")

# Iniciar el juego
if __name__ == "__main__":
    main()

ventana.mainloop()
