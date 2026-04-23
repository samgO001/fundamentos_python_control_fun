"""
Ejercicio 5 – Docstrings
Conceptos: documentación de funciones, estilos de docstring, help()
"""

# Ejemplo 1: Docstring de una línea
def es_mayor_de_edad(edad):
    """Determina si una persona es mayor de edad (18 años o más)."""
    return edad >= 18

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))

# Ejemplo 2: Docstring estilo Google
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros (list): Una lista de valores numéricos

    Returns:
        float: El promedio de los números

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)

notas = [7, 8, 6, 9]
print(f"\nPromedio: {calcular_promedio(notas)}")

# Ejemplo 3: Acceder al docstring
print("\nDocstring de calcular_promedio:")
print(calcular_promedio.__doc__)

# Ejemplo 4: Docstring con raises y validación
def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a (float): El numerador
        b (float): El denominador

    Returns:
        float: El resultado de la división, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
        >>> dividir_seguro(10, 0)
        None
    """
    if b == 0:
        return None
    return a / b

print(f"10 / 2 = {dividir_seguro(10, 2)}")
print(f"10 / 0 = {dividir_seguro(10, 0)}")

# Ejemplo 5: help()
print("\nAyuda de dividir_seguro:")
help(dividir_seguro)