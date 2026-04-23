"""
Ejercicio 2 – Bucle for en colecciones
Conceptos: iterar listas, cadenas, diccionarios, enumerate()
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Iterar sobre una lista
# Objetivo: Iterar sobre una lista.
# Entrada: datos de ejemplo para Iterar sobre una lista.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

# Ejemplo 2: Iterar con enumerate()
# Objetivo: Iterar con enumerate().
# Entrada: datos de ejemplo para Iterar con enumerate().
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nLista con índices:")
nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# Ejemplo 3: Iterar sobre una cadena
# Objetivo: Iterar sobre una cadena.
# Entrada: datos de ejemplo para Iterar sobre una cadena.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nLetras de 'Python':")
for letra in "Python":
    print(letra, end=" ")
print()

# Ejemplo 4: Iterar sobre un diccionario
# Objetivo: Iterar sobre un diccionario.
# Entrada: datos de ejemplo para Iterar sobre un diccionario.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nDatos del usuario:")
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Ejemplo 5: Iterar solo valores
# Objetivo: Iterar solo valores.
# Entrada: datos de ejemplo para Iterar solo valores.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nSolo valores:")
for valor in usuario.values():
    print(valor)
