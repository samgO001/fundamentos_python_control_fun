"""
Ejercicio 3 – Declaración if-elif-else
Conceptos: múltiples condiciones, elif
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Número positivo, negativo o cero
# Objetivo: Número positivo, negativo o cero.
# Entrada: datos de ejemplo para Número positivo, negativo o cero.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejemplo 2: Calificaciones
# Objetivo: Calificaciones.
# Entrada: datos de ejemplo para Calificaciones.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
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
# Objetivo: Rango de edad.
# Entrada: datos de ejemplo para Rango de edad.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 45
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")
