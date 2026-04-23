"""
Ejercicio 1 – Bucle for y función range()
Conceptos: for básico, range(stop), range(start, stop), range(start, stop, step)
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: range() básico del 0 al 4
# Objetivo: range() básico del 0 al 4.
# Entrada: datos de ejemplo para range() básico del 0 al 4.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Números del 0 al 4:")
for i in range(5):
    print(i, end=" ")
print()

# Ejemplo 2: range() con inicio y fin
# Objetivo: range() con inicio y fin.
# Entrada: datos de ejemplo para range() con inicio y fin.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Números del 3 al 7:")
for i in range(3, 8):
    print(i, end=" ")
print()

# Ejemplo 3: Números pares del 2 al 10
# Objetivo: Números pares del 2 al 10.
# Entrada: datos de ejemplo para Números pares del 2 al 10.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Números pares del 2 al 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Ejemplo 4: Cuenta regresiva
# Objetivo: Cuenta regresiva.
# Entrada: datos de ejemplo para Cuenta regresiva.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("Cuenta regresiva:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Ejemplo 5: Suma de los primeros 10 números
# Objetivo: Suma de los primeros 10 números.
# Entrada: datos de ejemplo para Suma de los primeros 10 números.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma de los primeros 10 números es: {suma}")
