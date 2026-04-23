"""
Ejercicio 2 – Declaración if-else
Conceptos: if-else, decisiones binarias
"""

# Ejemplo 1: Votación
edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

# Ejemplo 2: Contraseña
contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

# Ejemplo 3: Par o impar
numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")