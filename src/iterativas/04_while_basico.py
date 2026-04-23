"""
Ejercicio 4 – Bucle while básico
Conceptos: while, condición booleana, variable de control
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Contador básico
# Objetivo: Contador básico.
# Entrada: datos de ejemplo para Contador básico.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Contador del 1 al 5:")
contador = 1
while contador <= 5:
    print(contador, end=" ")
    contador += 1
print()

# Ejemplo 2: Comparación while vs for
# Objetivo: Comparación while vs for.
# Entrada: datos de ejemplo para Comparación while vs for.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nSuma con while:")
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma del 1 al 10: {suma}")

# Ejemplo 3: Factorial con while
# Objetivo: Factorial con while.
# Entrada: datos de ejemplo para Factorial con while.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
numero = 5
resultado = 1
while numero > 0:
    resultado *= numero
    numero -= 1
print(f"\nEl factorial de 5 es: {resultado}")

# Ejemplo 4: Triángulo de asteriscos
# Objetivo: Triángulo de asteriscos.
# Entrada: datos de ejemplo para Triángulo de asteriscos.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\nTriángulo de asteriscos:")
fila = 1
while fila <= 5:
    print("*" * fila)
    fila += 1
