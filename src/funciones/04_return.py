"""
Ejercicio 4 – Sentencia return
Conceptos: retorno de valores, múltiples valores, retorno anticipado
"""

# Ejemplo 1: Return básico
def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado

print(f"Cuadrado de 4: {calcular_cuadrado(4)}")

# Ejemplo 2: Función sin return devuelve None
def saludar(nombre):
    print(f"Hola, {nombre}")

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")

# Ejemplo 3: Retorno de múltiples valores
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)
print(f"\nSuma: {suma}")
print(f"Promedio: {media}")
print(f"Mínimo: {menor}")
print(f"Máximo: {mayor}")

# Ejemplo 4: Retorno anticipado
def dividir_seguro(a, b):
    if b == 0:
        print("Error: División por cero")
        return None
    return a / b

print(f"\nDivisión 10/2: {dividir_seguro(10, 2)}")
print(f"División 10/0: {dividir_seguro(10, 0)}")

# Ejemplo 5: Return con calificaciones
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"
    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"
    return "Insuficiente"

print(f"\nNota 95: {obtener_calificacion(95)}")
print(f"Nota 75: {obtener_calificacion(75)}")
print(f"Nota 45: {obtener_calificacion(45)}")