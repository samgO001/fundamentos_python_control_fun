"""
Ejercicio 2 – Parámetros y argumentos
Conceptos: posicionales, predeterminados, por nombre
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Parámetros posicionales
# Objetivo: Parámetros posicionales.
# Entrada: datos de ejemplo para Parámetros posicionales.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def calcular_precio_final(precio_base, impuesto):
    """Calcula el precio final sumando el impuesto al precio base."""
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)
print(f"Precio final: {total}")

# Ejemplo 2: Parámetros con valores predeterminados
# Objetivo: Parámetros con valores predeterminados.
# Entrada: datos de ejemplo para Parámetros con valores predeterminados.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def saludar(nombre, mensaje="¡Bienvenido!"):
    """Imprime un saludo personalizado con mensaje opcional."""
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("María", "¿Cómo estás hoy?")

# Ejemplo 3: Argumentos por nombre
# Objetivo: Argumentos por nombre.
# Entrada: datos de ejemplo para Argumentos por nombre.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def dividir(dividendo, divisor):
    """Retorna el resultado de dividir `dividendo` entre `divisor`."""
    return dividendo / divisor

print(f"División posicional: {dividir(10, 2)}")
print(f"División por nombre: {dividir(divisor=2, dividendo=10)}")

# Ejemplo 4: Combinando tipos de parámetros
# Objetivo: Combinando tipos de parámetros.
# Entrada: datos de ejemplo para Combinando tipos de parámetros.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    """Calcula el pago total con tarifa y moneda configurables."""
    total = horas * tarifa
    return f"{total} {moneda}"

print(calcular_pago(40))
print(calcular_pago(35, 20))
print(calcular_pago(30, moneda="USD"))
print(calcular_pago(horas=25, tarifa=18, moneda="GBP"))
