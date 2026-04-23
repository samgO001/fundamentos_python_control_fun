"""
Ejercicio 7 – Sentencias pass y else en bucles
Conceptos: pass como marcador, else se ejecuta si no hubo break
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: pass en bucle
# Objetivo: pass en bucle.
# Entrada: datos de ejemplo para pass en bucle.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print(" pass ")
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los pares
    else:
        print(f"Número impar: {numero}")

# Ejemplo 2: else en for - elemento no encontrado
# Objetivo: else en for - elemento no encontrado.
# Entrada: datos de ejemplo para else en for - elemento no encontrado.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\n else en for ")
numeros = [4, 6, 8, 9, 10, 12]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista.")

# Ejemplo 3: else en for - elemento encontrado (no ejecuta else)
# Objetivo: else en for - elemento encontrado (no ejecuta else).
# Entrada: datos de ejemplo para else en for - elemento encontrado (no ejecuta else).
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\n else no se ejecuta con break ")
numeros = [4, 6, 7, 8, 10]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado: {num}!")
        break
else:
    print("No se encontró ningún número primo.")

# Ejemplo 4: else en while
# Objetivo: else en while.
# Entrada: datos de ejemplo para else en while.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\n else en while ")
contador = 0
while contador < 5:
    print(f"Iteración {contador}")
    contador += 1
else:
    print("El while terminó normalmente.")
