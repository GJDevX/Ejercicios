from math import sqrt, pi

def circulo(radio: int) -> int:
    return pi*radio**2

def rectangulo(largo : int, ancho: int) -> int:
    return largo*ancho

def area_hexagono(lado: int) -> int:
    area = (3*sqrt(3)*lado**2)/2
    return area 

def area_totoal(hexagono, circulo, rectangulo):
    return hexagono + circulo + rectangulo 

def main():
    input("presione cualquier tecla para empezar")
    lado_hexagono = int(input("Ingrese el lado del Hexagono: "))
    radio_circulo = int(input("ingrese el radio del circulo: "))
    lado_rectangulo = int(input("Ingrese el lado del rectangulo: "))
    areas_hexagono = 0
    
    for hexagono in range(3):
        lado_hexagono = int(input("ingrese el lado del hexagono: "))
        area_hexagonos += area_hexagono(lado_hexagono)
    
    for circulo in range(2):
        area_circulo = int(input("Ingrese el radio del circulo: "))
    