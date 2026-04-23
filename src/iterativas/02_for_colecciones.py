"""
Ejercicio 2 – Bucle for en colecciones
Conceptos: iterar listas, cadenas, diccionarios, enumerate()
"""

# Ejemplo 1: Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

# Ejemplo 2: Iterar con enumerate()
print("\nLista con índices:")
nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# Ejemplo 3: Iterar sobre una cadena
print("\nLetras de 'Python':")
for letra in "Python":
    print(letra, end=" ")
print()

# Ejemplo 4: Iterar sobre un diccionario
print("\nDatos del usuario:")
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Ejemplo 5: Iterar solo valores
print("\nSolo valores:")
for valor in usuario.values():
    print(valor)