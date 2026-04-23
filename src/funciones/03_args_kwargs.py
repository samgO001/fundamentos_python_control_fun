"""
Ejercicio 3 – *args y **kwargs
Conceptos: número variable de argumentos posicionales y por nombre
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: *args - argumentos posicionales variables
# Objetivo: *args - argumentos posicionales variables.
# Entrada: datos de ejemplo para *args - argumentos posicionales variables.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def sumar(*numeros):
    """Suma una cantidad variable de números."""
    total = 0
    for numero in numeros:
        total += numero
    return total

print(f"Suma de 1, 2: {sumar(1, 2)}")
print(f"Suma de 1, 2, 3, 4, 5: {sumar(1, 2, 3, 4, 5)}")
print(f"Suma vacía: {sumar()}")

# Ejemplo 2: **kwargs - argumentos por nombre variables
# Objetivo: **kwargs - argumentos por nombre variables.
# Entrada: datos de ejemplo para **kwargs - argumentos por nombre variables.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def mostrar_informacion(**datos):
    """Imprime pares clave-valor recibidos como argumentos nombrados."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

print("\nInformación de Python:")
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)

# Ejemplo 3: Combinando *args y **kwargs
# Objetivo: Combinando *args y **kwargs.
# Entrada: datos de ejemplo para Combinando *args y **kwargs.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def describir_persona(*args, **kwargs):
    """Muestra datos posicionales y datos por nombre de una persona."""
    print("\nDatos posicionales:")
    for dato in args:
        print(f"  {dato}")
    print("Datos por nombre:")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

describir_persona("Ana", "Desarrolladora",
                  ciudad="Bogotá", edad=28, lenguaje="Python")
