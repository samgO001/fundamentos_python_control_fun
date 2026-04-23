"""
Ejercicio 4 – Bucle while básico
Conceptos: while, condición booleana, variable de control
"""

# Ejemplo 1: Contador básico
print("Contador del 1 al 5:")
contador = 1
while contador <= 5:
    print(contador, end=" ")
    contador += 1
print()

# Ejemplo 2: Comparación while vs for
print("\nSuma con while:")
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma del 1 al 10: {suma}")

# Ejemplo 3: Factorial con while
numero = 5
resultado = 1
while numero > 0:
    resultado *= numero
    numero -= 1
print(f"\nEl factorial de 5 es: {resultado}")

# Ejemplo 4: Triángulo de asteriscos
print("\nTriángulo de asteriscos:")
fila = 1
while fila <= 5:
    print("*" * fila)
    fila += 1