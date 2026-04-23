"""
Ejercicio 1 – Definición básica de funciones
Conceptos: def, llamada de función, reutilización de código
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Función simple sin parámetros
# Objetivo: Función simple sin parámetros.
# Entrada: datos de ejemplo para Función simple sin parámetros.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def saludar():
    """Imprime un saludo básico en consola."""
    print("¡Hola, mundo!")

saludar()

# Ejemplo 2: Función con parámetros
# Objetivo: Función con parámetros.
# Entrada: datos de ejemplo para Función con parámetros.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")

# Ejemplo 3: Función que verifica si un número es par
# Objetivo: Función que verifica si un número es par.
# Entrada: datos de ejemplo para Función que verifica si un número es par.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def es_par(numero):
    """Retorna True si `numero` es par, de lo contrario False."""
    return numero % 2 == 0

print(f"¿El 4 es par? {es_par(4)}")
print(f"¿El 7 es par? {es_par(7)}")

# Ejemplo 4: Función de conversión
# Objetivo: Función de conversión.
# Entrada: datos de ejemplo para Función de conversión.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a grados Fahrenheit."""
    return (celsius * 9/5) + 32

print(f"25°C equivalen a {celsius_a_fahrenheit(25)}°F")

# Ejemplo 5: Asignar función a una variable
# Objetivo: Asignar función a una variable.
# Entrada: datos de ejemplo para Asignar función a una variable.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
convertir = celsius_a_fahrenheit
print(f"Usando variable: 100°C equivalen a {convertir(100)}°F")
