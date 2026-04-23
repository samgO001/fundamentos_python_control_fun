"""
Ejercicio 2 – Parámetros y argumentos
Conceptos: posicionales, predeterminados, por nombre
"""

# Ejemplo 1: Parámetros posicionales
def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)
print(f"Precio final: {total}")

# Ejemplo 2: Parámetros con valores predeterminados
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("María", "¿Cómo estás hoy?")

# Ejemplo 3: Argumentos por nombre
def dividir(dividendo, divisor):
    return dividendo / divisor

print(f"División posicional: {dividir(10, 2)}")
print(f"División por nombre: {dividir(divisor=2, dividendo=10)}")

# Ejemplo 4: Combinando tipos de parámetros
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

print(calcular_pago(40))
print(calcular_pago(35, 20))
print(calcular_pago(30, moneda="USD"))
print(calcular_pago(horas=25, tarifa=18, moneda="GBP"))