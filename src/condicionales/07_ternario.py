"""
Ejercicio 7 – Expresión condicional (ternario)
Conceptos: valor_si_verdadero if condición else valor_si_falso
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Mayor de edad
# Objetivo: Mayor de edad.
# Entrada: datos de ejemplo para Mayor de edad.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)

# Ejemplo 2: Número mayor entre dos
# Objetivo: Número mayor entre dos.
# Entrada: datos de ejemplo para Número mayor entre dos.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
a = 1
b = 2
print("El máximo es:", a if a > b else b)

# Ejemplo 3: Ternario anidado
# Objetivo: Ternario anidado.
# Entrada: datos de ejemplo para Ternario anidado.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

# Ejemplo 4: Evitar división por cero
# Objetivo: Evitar división por cero.
# Entrada: datos de ejemplo para Evitar división por cero.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)

# Ejemplo 5: Lista por comprensión con ternario
# Objetivo: Lista por comprensión con ternario.
# Entrada: datos de ejemplo para Lista por comprensión con ternario.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)
