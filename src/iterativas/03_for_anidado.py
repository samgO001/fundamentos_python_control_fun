"""
Ejercicio 3 – Bucles for anidados
Conceptos: for dentro de for, matrices, comprensión de listas
"""

# Ejemplo 1: Tabla de multiplicar 3x3
print("Tabla de multiplicar 3x3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()

# Ejemplo 2: Comprensión de listas - cuadrados
cuadrados = [x**2 for x in range(1, 6)]
print(f"\nCuadrados del 1 al 5: {cuadrados}")

# Ejemplo 3: Comprensión de listas - filtrar pares
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares del 0 al 9: {pares}")

# Ejemplo 4: Temperaturas - día más caluroso
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