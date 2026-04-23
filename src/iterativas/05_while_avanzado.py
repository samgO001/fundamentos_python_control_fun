"""
Ejercicio 5 – While avanzado
Conceptos: bucle infinito, validación de entrada, eventos
"""

# Ejemplo 1: Validación de entrada
print("=== Validación de entrada ===")
entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número entero: ")
print(f"Has introducido el número: {entrada}")

# Ejemplo 2: Bucle infinito controlado
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