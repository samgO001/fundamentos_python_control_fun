"""
Ejercicio 5 – Docstrings
Conceptos: documentación de funciones, estilos de docstring, help()
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Docstring de una línea
# Objetivo: Docstring de una línea.
# Entrada: datos de ejemplo para Docstring de una línea.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def es_mayor_de_edad(edad):
    """Determina si una persona es mayor de edad (18 años o más)."""
    return edad >= 18

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))

# Ejemplo 2: Docstring estilo Google
# Objetivo: Docstring estilo Google.
# Entrada: datos de ejemplo para Docstring estilo Google.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
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
# Objetivo: Acceder al docstring.
# Entrada: datos de ejemplo para Acceder al docstring.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nDocstring de calcular_promedio:")
print(calcular_promedio.__doc__)

# Ejemplo 4: Docstring con validación de entrada
# Objetivo: Docstring con validación de entrada.
# Entrada: datos de ejemplo para Docstring con validación de entrada.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a (float): El numerador
        b (float): El denominador

    Returns:
        float | None: El resultado de la división, o None si b es cero

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
# Objetivo: help().
# Entrada: datos de ejemplo para help().
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nAyuda de dividir_seguro:")
help(dividir_seguro)
