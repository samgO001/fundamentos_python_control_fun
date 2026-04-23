"""
Ejercicio 4 – Sentencia return
Conceptos: retorno de valores, múltiples valores, retorno anticipado
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Return básico
# Objetivo: Return básico.
# Entrada: datos de ejemplo para Return básico.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def calcular_cuadrado(numero):
    """Devuelve el cuadrado del número recibido."""
    resultado = numero * numero
    return resultado

print(f"Cuadrado de 4: {calcular_cuadrado(4)}")

# Ejemplo 2: Función sin return devuelve None
# Objetivo: Función sin return devuelve None.
# Entrada: datos de ejemplo para Función sin return devuelve None.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def saludar(nombre):
    """Imprime un saludo y retorna None de forma implícita."""
    print(f"Hola, {nombre}")

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")

# Ejemplo 3: Retorno de múltiples valores
# Objetivo: Retorno de múltiples valores.
# Entrada: datos de ejemplo para Retorno de múltiples valores.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def estadisticas(numeros):
    """Retorna suma, promedio, mínimo y máximo de una lista numérica."""
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
# Objetivo: Retorno anticipado.
# Entrada: datos de ejemplo para Retorno anticipado.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def dividir_seguro(a, b):
    """Realiza una división y evita error cuando el divisor es cero."""
    if b == 0:
        print("Error: División por cero")
        return None
    return a / b

print(f"\nDivisión 10/2: {dividir_seguro(10, 2)}")
print(f"División 10/0: {dividir_seguro(10, 0)}")

# Ejemplo 5: Return con calificaciones
# Objetivo: Return con calificaciones.
# Entrada: datos de ejemplo para Return con calificaciones.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def obtener_calificacion(puntuacion):
    """Convierte una puntuación (0-100) en una etiqueta de desempeño."""
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
