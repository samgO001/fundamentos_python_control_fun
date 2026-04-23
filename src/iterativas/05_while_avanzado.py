"""
Ejercicio 5 – While avanzado
Conceptos: bucle infinito, validación de entrada, eventos
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Validación de entrada
# Objetivo: Validación de entrada.
# Entrada: datos de ejemplo para Validación de entrada.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("=== Validación de entrada ===")
entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número entero: ")
print(f"Has introducido el número: {entrada}")

# Ejemplo 2: Bucle infinito controlado
# Objetivo: Bucle infinito controlado.
# Entrada: datos de ejemplo para Bucle infinito controlado.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
print("\n Menú de opciones ")
while True:
    print("\n1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Hasta luego!")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
