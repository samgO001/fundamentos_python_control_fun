"""
Ejercicio 7 – Sentencias pass y else en bucles
Conceptos: pass como marcador, else se ejecuta si no hubo break
"""

# Ejemplo 1: pass en bucle
print(" pass ")
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los pares
    else:
        print(f"Número impar: {numero}")

# Ejemplo 2: else en for - elemento no encontrado
print("\n else en for ")
numeros = [4, 6, 8, 9, 10, 12]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista.")

# Ejemplo 3: else en for - elemento encontrado (no ejecuta else)
print("\n else no se ejecuta con break ")
numeros = [4, 6, 7, 8, 10]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado: {num}!")
        break
else:
    print("No se encontró ningún número primo.")

# Ejemplo 4: else en while
print("\n else en while ")
contador = 0
while contador < 5:
    print(f"Iteración {contador}")
    contador += 1
else:
    print("El while terminó normalmente.")