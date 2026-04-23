# Fundamentos Python – Estructuras de Control y Funciones

Proyecto desarrollado como evidencia de aprendizaje de la actividad GA1 220501093-04 AA1 EV02.
Integra los conceptos esenciales de Python: estructuras condicionales, iterativas y funciones.



## Estructura del proyecto

fundamentos_python_control_fun/
└── src/
├── condicionales/
├── iterativas/
└── funciones/

## Cómo ejecutar los ejercicios

Desde la raíz del proyecto ejecuta:

```bash
python src/<carpeta>/<archivo>.py
```

Ejemplo:
```bash
python src/condicionales/01_if_basico.py
```

---

## Condicionales

### 01_if_basico.py
Muestra el uso de la declaración `if` simple. Evalúa condiciones como
la mayoría de edad, temperatura y saludos según la hora del día.
```bash
python src/condicionales/01_if_basico.py
```

### 02_if_else.py
Implementa decisiones binarias con `if-else`. Incluye verificación de
votación, validación de contraseña y detección de números pares e impares.
Este ejercicio pide ingresar una contraseña por teclado.
```bash
python src/condicionales/02_if_else.py
```

### 03_if_elif_else.py
Evalúa múltiples condiciones con `if-elif-else`. Clasifica números
como positivos, negativos o cero, asigna calificaciones y determina
rangos de edad.
```bash
python src/condicionales/03_if_elif_else.py
```

### 04_match_case.py
Utiliza la declaración `match-case` de Python 3.10. Clasifica frutas,
evalúa coordenadas y gestiona roles de usuario.
Este ejercicio pide ingresar una fruta por teclado.
```bash
python src/condicionales/04_match_case.py
```

### 05_operadores_logicos.py
Demuestra el uso de `and`, `or` y `not` para combinar condiciones.
Incluye ejemplos de elegibilidad para crédito, fin de semana y
licencia de conducir con permiso parental.
```bash
python src/condicionales/05_operadores_logicos.py
```

### 06_condicionales_anidados.py
Implementa `if` dentro de `if` para manejar jerarquías de condiciones.
Cubre clasificación por edad y estado civil, licencia de conducir y
sistema de login.
```bash
python src/condicionales/06_condicionales_anidados.py
```

### 07_ternario.py
Aplica expresiones condicionales en una sola línea. Incluye
verificación de edad, valor máximo, categorías anidadas, prevención
de división por cero y listas por comprensión.
```bash
python src/condicionales/07_ternario.py
```

### 08_cortocircuito.py
Explica cómo Python evita evaluar condiciones innecesarias con `and`
y `or`. Previene errores de índice y división por cero, y usa
`any()` y `all()`.
```bash
python src/condicionales/08_cortocircuito.py
```

---

## Iterativas

### 01_for_range.py
Introduce el bucle `for` con la función `range()`. Recorre secuencias
numéricas con inicio, fin y paso, incluyendo cuenta regresiva y
cálculo de suma acumulada.
```bash
python src/iterativas/01_for_range.py
```

### 02_for_colecciones.py
Itera sobre listas, cadenas y diccionarios. Usa `enumerate()` para
obtener índices, recorre letras de una cadena y accede a claves y
valores de un diccionario.
```bash
python src/iterativas/02_for_colecciones.py
```

### 03_for_anidado.py
Trabaja con bucles `for` anidados y comprensión de listas. Genera
una tabla de multiplicar, crea listas de cuadrados, filtra pares y
analiza temperaturas semanales.
```bash
python src/iterativas/03_for_anidado.py
```

### 04_while_basico.py
Implementa el bucle `while` con variable de control. Incluye contador,
suma acumulada, cálculo de factorial y generación de un triángulo de
asteriscos.
```bash
python src/iterativas/04_while_basico.py
```

### 05_while_avanzado.py
Aplica `while` para validación de entrada y menús interactivos.
Incluye un bucle infinito controlado con `break` y un menú de
opciones por consola.
Este ejercicio requiere interacción por teclado.
```bash
python src/iterativas/05_while_avanzado.py
```

### 06_break_continue.py
Demuestra el uso de `break` para salir del bucle y `continue` para
saltar iteraciones. Incluye búsqueda de elementos, filtrado de
temperaturas negativas y combinación de ambas sentencias.
```bash
python src/iterativas/06_break_continue.py
```

### 07_pass_else.py
Explica `pass` como marcador de posición y la cláusula `else` en
bucles. Muestra cuándo se ejecuta `else` (sin `break`) y cuándo no,
tanto en `for` como en `while`.
```bash
python src/iterativas/07_pass_else.py
```

---

## Funciones

### 01_funciones_basicas.py
Introduce la definición y llamada de funciones con `def`. Incluye
funciones sin parámetros, con parámetros, con `return` y asignación
de funciones a variables.
```bash
python src/funciones/01_funciones_basicas.py
```

### 02_parametros_argumentos.py
Diferencia entre parámetros posicionales, con valores predeterminados
y argumentos por nombre. Muestra cuatro formas distintas de llamar a
una misma función.
```bash
python src/funciones/02_parametros_argumentos.py
```

### 03_args_kwargs.py
Implementa funciones con número variable de argumentos usando `*args`
(tupla de posicionales) y `**kwargs` (diccionario de argumentos por
nombre), y su combinación.
```bash
python src/funciones/03_args_kwargs.py
```

### 04_return.py
Profundiza en la sentencia `return`. Cubre retorno simple, funciones
sin return que devuelven `None`, retorno de múltiples valores,
retorno anticipado y calificaciones con returns tempranos.
```bash
python src/funciones/04_return.py
```

### 05_docstrings.py
Documenta funciones con docstrings de una línea y multilínea estilo
Google. Accede a la documentación con `__doc__` y `help()`, y muestra
buenas prácticas de documentación.
```bash
python src/funciones/05_docstrings.py
