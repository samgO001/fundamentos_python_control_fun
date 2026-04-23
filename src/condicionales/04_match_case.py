"""
Ejercicio 4 – Declaración match-case
Conceptos: coincidencia de patrones, case, comodín _
Requiere Python 3.10 o superior
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Clasificar frutas
# Objetivo: Clasificar frutas.
# Entrada: datos de ejemplo para Clasificar frutas.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
fruta = input("Introduce una fruta: ")
match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "platano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

# Ejemplo 2: Coordenadas
# Objetivo: Coordenadas.
# Entrada: datos de ejemplo para Coordenadas.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
punto = (0, 0)
match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")

# Ejemplo 3: Roles de usuario
# Objetivo: Roles de usuario.
# Entrada: datos de ejemplo para Roles de usuario.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
usuario = {"nombre": "Ana", "rol": "admin"}
match usuario:
    case {"rol": "admin"}:
        print(f"{usuario['nombre']} tiene permisos de administrador.")
    case {"rol": "moderador"}:
        print(f"{usuario['nombre']} puede moderar contenidos.")
    case {"rol": "usuario"}:
        print(f"{usuario['nombre']} es un usuario regular.")
    case _:
        print("Rol desconocido.")
