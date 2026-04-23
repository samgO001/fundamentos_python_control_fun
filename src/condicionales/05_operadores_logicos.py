"""
Ejercicio 5 – Operadores lógicos
Conceptos: and, or, not y su combinación
"""

# Descripcion del archivo: ejemplos practicos del tema indicado.
# Nota: cada bloque muestra una situacion concreta y su salida esperada.

# Ejemplo 1: Operador and
# Objetivo: Operador and.
# Entrada: datos de ejemplo para Operador and.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 25
ingresos = 30000
if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")

# Ejemplo 2: Operador or
# Objetivo: Operador or.
# Entrada: datos de ejemplo para Operador or.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

# Ejemplo 3: Operador not
# Objetivo: Operador not.
# Entrada: datos de ejemplo para Operador not.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
llueve = False
if not llueve:
    print("Podemos salir al parque.")

# Ejemplo 4: Combinación de operadores
# Objetivo: Combinación de operadores.
# Entrada: datos de ejemplo para Combinación de operadores.
# Proceso: se evalua la condicion o se ejecuta el bloque correspondiente.
# Salida: mensaje en consola segun el resultado del ejemplo.
edad = 17
permiso_parental = True
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")
