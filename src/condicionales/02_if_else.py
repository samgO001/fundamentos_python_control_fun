"""
Ejercicio 2 – Declaración if-else
Conceptos: if-else, decisiones binarias
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Votación
# Objetivo: Votación.
# Entrada: datos de ejemplo para Votación.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

# Ejemplo 2: Contraseña
# Objetivo: Contraseña.
# Entrada: datos de ejemplo para Contraseña.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

# Ejemplo 3: Par o impar
# Objetivo: Par o impar.
# Entrada: datos de ejemplo para Par o impar.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
