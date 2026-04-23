"""
Ejercicio 1 – Definición básica de funciones
Conceptos: def, llamada de función, reutilización de código
"""

# Ejemplo 1: Función simple sin parámetros
def saludar():
    print("¡Hola, mundo!")

saludar()

# Ejemplo 2: Función con parámetros
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")

# Ejemplo 3: Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

print(f"¿El 4 es par? {es_par(4)}")
print(f"¿El 7 es par? {es_par(7)}")

# Ejemplo 4: Función de conversión
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(f"25°C equivalen a {celsius_a_fahrenheit(25)}°F")

# Ejemplo 5: Asignar función a una variable
convertir = celsius_a_fahrenheit
print(f"Usando variable: 100°C equivalen a {convertir(100)}°F")