"""
Ejercicio 3 – *args y **kwargs
Conceptos: número variable de argumentos posicionales y por nombre
"""

# Ejemplo 1: *args - argumentos posicionales variables
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(f"Suma de 1, 2: {sumar(1, 2)}")
print(f"Suma de 1, 2, 3, 4, 5: {sumar(1, 2, 3, 4, 5)}")
print(f"Suma vacía: {sumar()}")

# Ejemplo 2: **kwargs - argumentos por nombre variables
def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

print("\nInformación de Python:")
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)

# Ejemplo 3: Combinando *args y **kwargs
def describir_persona(*args, **kwargs):
    print("\nDatos posicionales:")
    for dato in args:
        print(f"  {dato}")
    print("Datos por nombre:")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

describir_persona("Ana", "Desarrolladora",
                  ciudad="Bogotá", edad=28, lenguaje="Python")