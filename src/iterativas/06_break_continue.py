"""
Ejercicio 6 – Sentencias break y continue
Conceptos: break termina el bucle, continue salta la iteración actual
"""

# Ejemplo 1: break - salir al encontrar un número
print(" break ")
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

# Ejemplo 2: continue - saltar números pares
print("\n continue ")
for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Número impar: {numero}")

# Ejemplo 3: Filtrar temperaturas negativas
print("\n Filtrar temperaturas positivas ")
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]
for temp in temperaturas:
    if temp <= 0:
        continue
    print(f"{temp}°C")

# Ejemplo 4: Combinando break y continue
print("\n Combinando break y continue ")
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0
for num in numeros:
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")
    if suma > limite:
        print(f"Límite de {limite} superado")
        break