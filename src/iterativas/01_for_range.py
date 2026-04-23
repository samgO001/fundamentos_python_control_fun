"""
Ejercicio 1 – Bucle for y función range()
Conceptos: for básico, range(stop), range(start, stop), range(start, stop, step)
"""

# Ejemplo 1: range() básico del 0 al 4
print("Números del 0 al 4:")
for i in range(5):
    print(i, end=" ")
print()

# Ejemplo 2: range() con inicio y fin
print("Números del 3 al 7:")
for i in range(3, 8):
    print(i, end=" ")
print()

# Ejemplo 3: Números pares del 2 al 10
print("Números pares del 2 al 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Ejemplo 4: Cuenta regresiva
print("Cuenta regresiva:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Ejemplo 5: Suma de los primeros 10 números
suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma de los primeros 10 números es: {suma}")