
# Manejo de funciones en Python

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO
"""
    1. ¿Qué es una función en Python y para qué sirve?
        Una función en Python es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten 
        organizar y modularizar el código, lo que facilita su mantenimiento y reutilización.

    2. ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
        Los parámetros son las variables definidas en la declaración de la función, mientras que los argumentos son los 
        valores que se pasan a la función cuando se llama.

    3. ¿Por qué es útil separar la lógica en funciones reutilizables?
        Separar la lógica en funciones hace que el código sea más limpio, modular y reutilizable. Esto facilita la 
        depuración y el mantenimiento del código, además de permitir su reutilización en diferentes partes del programa.

    4. ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
        Un valor de retorno es el valor que una función regresa cuando termina su ejecución. Es mejor devolver resultados 
        porque permite que la función sea utilizada en diferentes contextos y se pueda manipular el valor antes de ser mostrado.

    5. ¿Qué cubrirá tu documento?
        Este documento cubre la descripción de cada problema, el diseño de funciones, las entradas y salidas, las validaciones 
        y los casos de prueba básicos para cada uno de los problemas planteados.
"""

# PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    1. Preferir funciones pequeñas que hagan una sola cosa (single responsibility).
    2. Evitar repetir código: si copias/pegas lógica, considera extraerla en una función.
    3. Intentar que las funciones sean “puras” cuando sea posible (mismo input -> mismo output, sin efectos secundarios externos).
    4. Documentar con comentarios simples qué hace cada función y qué parámetros espera.
    5. Dar nombres claros a las funciones (calculate_bmi, not f1 o do_it).
"""

# PROBLEM 1: Rectangle area and perimeter

    # Description:
        #Define dos funciones
        # - calculate_area(width, height): regresa el área de un rectángulo.
        # - calculate_perimeter(width, height): regresa el perímetro.
        # El código principal debe leer (o definir) los valores, llamar a las 
        # funciones y mostrar los resultados.
    # Inputs:
        # - width (float)
        # - height (float)
    # Outputs:
        # - "Area:" <area_value>
        # - "Perimeter:" <perimeter_value>
    # Validations:  
        # - width > 0
        # - height > 0
        # - Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.
# TESTE CASES:
     # Normal:
#    Input: width = 5, height = 3
#    Output: Area: 15 | Perimeter: 16
#
     # Border:
#    Input: width = 1, height = 1
#    Output: Area: 1 | Perimeter: 4
#
     # Error:
#    Input: width = -2, height = 4
#    Output: Error: invalid input

# CODE:

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)


try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)

        print("Area:", area)
        print("Perimeter:", perimeter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

# PROBLEM 2: Grade classifier
    # Description:
        # Define una función classify_grade(score) que reciba una calificación numérica 
        # (0–100) y regrese una categoría:
        # - "A" si score >= 90
        # - "B" si 80 <= score < 90
        # - "C" si 70 <= score < 80
        # - "D" si 60 <= score < 70
        # - "F" si score < 60
        # El código principal debe llamar la función y mostrar el resultado.
    # Inputs:
        # - score (float or int)
    # Outputs:
        # - "Score:" <score>
        # - "Category:" <grade_letter>
        # - If invalid: "Error: invalid input"
    # Validations:
        # - score must be convertible to float
        # - score must be between 0 and 100

# TEST CASES:
     # Normal:
#    Input: 85
#    Output: Score: 85 | Category: B
#
     # Border:
#    Input: 90
#    Output: Score: 90 | Category: A
#
     # Error:
#    Input: -5
#    Output: Error: invalid input

# CODE:

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter score (0-100): "))

    if 0 <= score <= 100:
        letter = classify_grade(score)
        print("Score:", score)
        print("Category:", letter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

# PROBLEM 3: - List statistics function (min, max, average)

    # Description:
        # Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
        #- "min": mínimo
        # - "max": máximo
        # - "average": promedio (float)
        # El código principal debe construir la lista (por ejemplo, a partir de 
        # texto separado por comas), llamar la función y mostrar los valores.
    # Inputs:
        # - numbers_text (string, e.g., "10,20,30")
        # - numbers_list (list of float or int, created internally)
    # Outputs:
        # - "Min:" <min_value>
        # - "Max:" <max_value>
        # - "Average:" <average_value>
        # - If invalid: "Error: invalid input"
    # Validations:
        # - numbers_text must not be empty
        # - numbers_list must not be empty
        # - all values must be valid number
# TEST CASE:
     # Normal:
#    Input: "10,20,30"
#    Output: Min: 10 | Max: 30 | Average: 20.0
#
     # Border:
#    Input: "5"
#    Output: Min: 5 | Max: 5 | Average: 5.0
#
     # Error:
#    Input: "10,abc,30"
#    Output: Error: invalid input

# CODE:

def summarize_numbers(numbers_list):
    info = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return info


numbers_text = input("Enter numbers separated by commas: ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            num = float(p)
            numbers_list.append(num)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: invalid input")

# Problem #: 4 - Apply discount list (pure function)

    # Description:
        # Define una función apply_discount(prices_list, discount_rate) que:
        # - reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
        # - regrese una nueva lista con los precios ya descontados (no modificar la lista original).
        # El código principal debe:
        #- Crear una lista de precios.
        # - Llamar a la función.
        #- Mostrar la lista original y la nueva lista con descuento.
    # Inputs:
        # - prices_text (string, e.g., "100,200,300")
        # - discount_rate (float between 0 and 1)
    # Outputs:
        # - "Original prices:" <original_list>
        # - "Discounted prices:" <discounted_list>
        # - If invalid: "Error: invalid input"
    # Validations:
        # - prices_text not empty
        # - all prices > 0
        # - discount_rate between 0 and 1
        # - list must not be empty

# TEST CASE:
     # Normal:
#    Input: "100,200,300", discount_rate = 0.10
#    Output: Original prices: [100.0, 200.0, 300.0]
#            Discounted prices: [90.0, 180.0, 270.0]
     # Border:
#    Input: "50", discount_rate = 0
#    Output: Original prices: [50.0]
#            Discounted prices: [50.0]

     # Error:
#    Input: "100,abc,300", discount_rate = 0.20
#    Output: Error: invalid input

# CODE:

def apply_discount(prices_list, discount_rate):
    new_list = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        new_list.append(new_price)
    return new_list


prices_text = input("Enter prices separated by commas: ").strip()

if prices_text == "":
    print("Error: invalid input")
else:
    try:
        parts = prices_text.split(",")
        prices_list = []

        for p in parts:
            price = float(p)
            if price <= 0:
                raise ValueError
            prices_list.append(price)

        if len(prices_list) == 0:
            print("Error: invalid input")
        else:
            try:
                discount_rate = float(input("Enter discount rate (0 to 1): "))
                if discount_rate < 0 or discount_rate > 1:
                    print("Error: invalid input")
                else:
                    discounted = apply_discount(prices_list, discount_rate)
                    print("Original prices:", prices_list)
                    print("Discounted prices:", discounted)
            except ValueError:
                print("Error: invalid input")

    except ValueError:
        print("Error: invalid input")

# Problem #: 5 - Greeting function with default parameters
    # Description:
        # Define una función greet(name, title="") que:
        # - Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
        #- Regrese el mensaje: "Hello, <full_name>!"
        # Si title está vacío, solo usar el nombre. El código principal debe llamar a l
        # a función usando argumentos posicionales y nombrados.
    # Inputs:
        # - name (string)
        # - title (string, optional)
    # Outputs:
        # - "Greeting:" <greeting_message>
        # - If invalid: "Error: invalid input"

    # Validations:
        # - name not empty after strip()
        # - title can be empty, but should be stripped
# TEST CASE:
     # Normal:
#    Input: name="Alice", title="Dr."
#    Output: Greeting: Hello, Dr. Alice!
#
     # Border:
#    Input: name="Bob", title="" 
#    Output: Greeting: Hello, Bob!
#
     # Error:
#    Input: name="" (after strip)
#    Output: Error: invalid input

# CODE:

def greet(name, title=""):
    if title == "":
        full_name = name
    else:
        full_name = title + " " + name
    return f"Hello, {full_name}!"


name = input("Enter name: ").strip()

if name == "":
    print("Error: invalid input")
else:
    title = input("Enter title (optional): ").strip()

    # title can be empty, so no strict validation needed
    message = greet(name, title)
    print("Greeting:", message)

# Problem #: 6
    # Description:
        # Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
        #- Leer/definir n.
        #- Validar n.
        #- Llamar a factorial(n).
        #- Mostrar el resultado.
    # Inputs:
        #  n (int)
    # Outputs:
        # - "n:" <n>
        # - "Factorial:" <factorial_value>
    # Validations:
        # - n must be an integer.
        # - n >= 0.
        # - Optional limit: n <= 20 to avoid excessively large values.
# TEST CASE:
     # Normal:
#    Input: 5
#    Output: Factorial: 120
     # Border:
#    Input: 0
#    Output: Factorial: 1

     # Error:
#    Input: -3
#    Output: Error: invalid input

# CODE
def factorial(n):
    """
    Iterative factorial function:
    factorial(0) = 1
    factorial(n) = 1 * 2 * ... * n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    n_text = input("Enter an integer n: ").strip()

    if not n_text.lstrip("-").isdigit():
        print("Error: invalid input")
    else:
        n = int(n_text)

        if n < 0 or n > 20:
            print("Error: invalid input")
        else:
            value = factorial(n)
            print("n:", n)
            print("Factorial:", value)

except:
    print("Error: invalid input")

# CONCLUSIÓN
"""
    Las funciones ayudan a organizar el código, haciéndolo modular y reutilizable. 
    Devolver resultados con `return` permite manipular los valores de salida y hacer 
    uso de los resultados en diversas partes del programa, mientras que solo imprimirlos 
    limita su reutilización. Usar parámetros con valores por defecto hace el código más 
    flexible, permitiendo que las funciones manejen entradas opcionales. Encapsular cálculos 
    repetidos en funciones facilita el mantenimiento del código y mejora la legibilidad.
"""
# REFERENCIAS
# 1) Python Official Documentation – Functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) W3Schools – Python Functions Tutorial:
#    https://www.w3schools.com/python/python_functions.asp
# 3) Real Python – Defining and Using Functions:
#    https://realpython.com/defining-your-own-python-function/
# 4) GeeksforGeeks – Python Functions:
#    https://www.geeksforgeeks.org/python-functions/
# 5) Programiz – Python Function Examples:
#    https://www.programiz.com/python-programming/function

# REPOSITORIO DE GITHUB
# https://github.com/maldonadoacunajuliocesar/metodologias_de_la_programaci-n/blob/main/src/2530001_Maldonado_Acu%C3%B1a_Julio_C%C3%A9sar.py
