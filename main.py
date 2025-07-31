def suma(a, b):
    """
    Calcula la suma de dos números.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La suma de los dos números
    """
    return a + b

# Ejemplos de uso
print("Ejemplos de suma:")
print(f"2 + 3 = {suma(2, 3)}")
print(f"10 + 5 = {suma(10, 5)}")
print(f"-1 + 1 = {suma(-1, 1)}")


def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


print(suma(1, 2))
print(resta(1, 2))


def saludar(nombre):
    mensaje = f"Hola, {nombre}"
    return mensaje

print(saludar("Juan"))
print(saludar("Pedro"))


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
print(es_primo(7))

import random

def obtener_jugada_computadora():
    return random.choice(["piedra", "papel", "tijera"]) 

print(obtener_jugada_computadora())


def celcius_a_fahrenheit(celcius):
    return (celcius * 9/5) + 32 

print(celcius_a_fahrenheit(100))    











