"""
Ejercicio 6 – Condicionales anidados
Conceptos: if dentro de if, jerarquía de condiciones
"""

# Ejemplo 1: Edad y estado civil
edad = 30
estado_civil = "soltero"
if edad >= 18:
    if estado_civil == "casado":
        print("Eres un adulto casado.")
    else:
        print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.")

# Ejemplo 2: Licencia de conducir
edad = 16
permiso_padres = True
if edad >= 18:
    print("Puedes obtener la licencia de conducir.")
else:
    if edad >= 16:
        if permiso_padres:
            print("Puedes obtener la licencia con permiso de tus padres.")
        else:
            print("Necesitas el permiso de tus padres para obtener la licencia.")
    else:
        print("Eres demasiado joven para conducir.")

# Ejemplo 3: Login
usuario = "admin"
contrasena = "1234"
if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no reconocido.")