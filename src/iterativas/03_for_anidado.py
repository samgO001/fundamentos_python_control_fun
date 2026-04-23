"""
Ejercicio 3 – Bucles for anidados
Conceptos: for dentro de for, matrices, comprensión de listas
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Tabla de multiplicar 3x3
# Objetivo: Tabla de multiplicar 3x3.
# Entrada: datos de ejemplo para Tabla de multiplicar 3x3.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Tabla de multiplicar 3x3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()

# Ejemplo 2: Comprensión de listas - cuadrados
# Objetivo: Comprensión de listas - cuadrados.
# Entrada: datos de ejemplo para Comprensión de listas - cuadrados.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
cuadrados = [x**2 for x in range(1, 6)]
print(f"\nCuadrados del 1 al 5: {cuadrados}")

# Ejemplo 3: Comprensión de listas - filtrar pares
# Objetivo: Comprensión de listas - filtrar pares.
# Entrada: datos de ejemplo para Comprensión de listas - filtrar pares.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares del 0 al 9: {pares}")

# Ejemplo 4: Temperaturas - día más caluroso
# Objetivo: Temperaturas - día más caluroso.
# Entrada: datos de ejemplo para Temperaturas - día más caluroso.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"\nEl día más caluroso fue {dias[indice_max]} con {max_temp}°C")

promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

print("Días por encima del promedio:")
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"  {dias[i]}: {temperaturas[i]}°C")
