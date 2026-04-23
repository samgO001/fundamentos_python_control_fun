"""
Ejercicio 8 – Evaluación de cortocircuito
Conceptos: and/or no evalúan la segunda condición si no es necesario
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Evitar IndexError con lista vacía
# Objetivo: Evitar IndexError con lista vacía.
# Entrada: datos de ejemplo para Evitar IndexError con lista vacía.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
lista = []
if lista and lista[0] == "Python":
    print("El primer elemento es 'Python'.")
else:
    print("La lista está vacía, no se evaluó lista[0].")

# Ejemplo 2: Evitar ZeroDivisionError
# Objetivo: Evitar ZeroDivisionError.
# Entrada: datos de ejemplo para Evitar ZeroDivisionError.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
dividendo = 10
divisor = 0
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

# Ejemplo 3: Cortocircuito con or
# Objetivo: Cortocircuito con or.
# Entrada: datos de ejemplo para Cortocircuito con or.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
acceso_permitido = False
acceso_registrado = True
if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# Ejemplo 4: any() y all()
# Objetivo: any() y all().
# Entrada: datos de ejemplo para any() y all().
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
numeros = [0, 0, 1, 0]
if any(numeros):
    print("Al menos un número es no cero.")

condiciones = [True, True, False, True]
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")
