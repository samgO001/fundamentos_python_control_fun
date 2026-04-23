"""
Ejercicio 8 – Evaluación de cortocircuito
Conceptos: and/or no evalúan la segunda condición si no es necesario
"""

# Ejemplo 1: Evitar IndexError con lista vacía
lista = []
if lista and lista[0] == "Python":
    print("El primer elemento es 'Python'.")
else:
    print("La lista está vacía, no se evaluó lista[0].")

# Ejemplo 2: Evitar ZeroDivisionError
dividendo = 10
divisor = 0
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

# Ejemplo 3: Cortocircuito con or
acceso_permitido = False
acceso_registrado = True
if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# Ejemplo 4: any() y all()
numeros = [0, 0, 1, 0]
if any(numeros):
    print("Al menos un número es no cero.")

condiciones = [True, True, False, True]
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")