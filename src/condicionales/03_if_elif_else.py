"""
Ejercicio 3 – Declaración if-elif-else
Conceptos: múltiples condiciones, elif
"""

# Ejemplo 1: Número positivo, negativo o cero
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejemplo 2: Calificaciones
nota = 87
if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

# Ejemplo 3: Rango de edad
edad = 45
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")