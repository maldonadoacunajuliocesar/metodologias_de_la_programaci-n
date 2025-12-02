# MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 

"""
    1. ¿Qué son los tipos int y float en Python y en qué se diferencian?
        Los tipos int y float son tipos numéricos en Python. El tipo int se 
        utiliza para representar números enteros (sin decimales), 

        El tipo float se utiliza para representar números con decimales. 
        La diferencia principal entre ambos radica en que los int son números enteros, 
        mientras que los float permiten almacenar valores con fracciones decimales.

    2. ¿Qué es un booleano (TRUE/FALSE) y cómo se obtiene en comparaciones?
        Un booleano es un tipo de dato que solo puede tener dos valores: True o False. 
        Los booleanos se obtienen a partir de comparaciones lógicas, como por ejemplo, 
        si una condición es verdadera (True) o falsa (False). 
        Estas comparaciones utilizan operadores relacionales como ==, >, <, >=, <=, etc.

    3. ¿Por qué es importante validar rangos y evitar división entre cero?
        Es importante validar rangos porque se debe asegurar que los datos ingresados estén 
        dentro de los valores esperados y evitar valores negativos o fuera de los límites
        válidos (por ejemplo, horas trabajadas o ingresos). Además, evitar la división 
        entre cero es crucial, ya que esta operación provoca un error en el programa y
        puede hacer que el sistema falle.

    4.  ¿Qué cubrirá tu documento?
        Este documento cubrirá la descripción de cada problema, el diseño de entradas y 
        salidas, las validaciones aplicadas y el uso de tipos de datos int, float y boolean 
        para realizar decisiones en los problemas. Se explicará cómo estos tipos numéricos y 
        booleanos permiten realizar cálculos, tomar decisiones lógicas y manejar situaciones de 
        validación en distintos escenarios.
"""
# PRINCIPIOS Y BUENAS PRÁCTICAS:
"""
    1. Usar tipos apropiados: int para contadores, float para cantidades con decimales.
    2. Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
    3. Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
    4. Usar nombres de variables descriptivos y mensajes claros para el usuario.
    5. Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).
"""

# PROBLEM 1: Temperatur converter and range flag 

   # Description:
       # Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. 
       # Además, determina un valor booleano is_high_temperature que sea true si la 
       # temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.
   # Inputs: 
       # temp_c (float; temperatura en °C).
   # Outputs: 
       # "Fahrenheit:" <temp_f>
       # "Kelvin:" <temp_k>
       # "High temperature:" true|false
   # Validations:
       # - Verificar que temp_c pueda convertirse a float.
       # - No permitir temperaturas físicas imposibles en 
       #  Kelvin (por ejemplo, temp_k < 0.0).

# TEST CASES: 
     # Normal:
"""
Temperature converter:

Enter the temperature in °C 30
Faherenheit: 86.00
Kelvin: 303.15
High Temperature:True
"""
     # Border:
"""
Temperature converter:

Enter the temperature in °C 25
Faherenheit: 77.00
Kelvin: 298.15
High Temperature:False
"""
     # Error:
"""
Temperature converter:

Enter the temperature in °C invalid
The temperature must be a valid value
"""

# CODE
print ("\nTemperature converter: \n" )
try:
    temp_c = float(input("Enter the temperature in °C"))
    temp_k = temp_c + 273.15

    if temp_k < 0.0: 
        print ("Impossible physical temperature")
    else: 
        temp_f = temp_c * 9/5 + 32
        is_high_temperature = (temp_c >= 30.0)

        print(f"Faherenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High Temperature:{str(is_high_temperature)}")
except: 
    print("The temperature must be a valid value")

# PROBLEM 2: Work hours and overtime payment 

   # Description:
       # Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a 
       # hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal.
       # Además, genera un booleano has_overtime que indique si 
       # el trabajador hizo horas extra.
   # Inputs: 
       # hours_worked (float; horas trabajadas en la semana).
       # hourly_rate (float; pago por hora).
   # Outputs: 
       # "Regular pay:" <regular_pay>
       # "Overtime pay:" <overtime_pay>
       # "Total pay:" <total_pay>
       # "Has overtime:" true|false
   # Validations:
       # - hours_worked >= 0
       # - hourly_rate > 0
       # - Si alguno no cumple, mostrar "Error: invalid input".

# TEST CASES: 
     # Normal:
"""
Work hourse and overtime payment:

Hours worked in the week: 45
Pay per hour: 20
Regular Pay: 800.0
Overtime pay: 150.0
Total Pay: 950.0
Has over time: True
"""
     # Border:
"""
Work hourse and overtime payment:

Hours worked in the week:40
Pay per hour:20
Regular Pay: 800.0
Overtime pay: 0.0
Total Pay: 800.0
Has over time: False
"""
     # Error:
"""
Work hourse and overtime payment:

Hours worked in the week: -5
Pay per hour:20
Error: Invalid Input
"""

# CODE
print ("\nWork hourse and overtime payment: \n")

try:
    hours_worked = float(input("Hours worked in the week:"))
    hourly_rate = float(input("Pay per hour:"))

    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, 40)
        overtime_hourse = max(hours_worked -40, 0)
        
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hourse * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime =  hours_worked > 40

        print (f"Regular Pay: {regular_pay}")
        print (f"Overtime pay: {overtime_pay}")
        print (f"Total Pay: {total_pay}")
        print (f"Has over time: {has_overtime}")
    else:
        print("Error: Invalid Input")
    
except:
     print ("Error: Invalid Input ")

# PROBLEM 3: Discount eligibility with booleans 

   # Description:
       # Determina si un cliente obtiene un descuento en su compra. La regla es:
       # Tiene descuento si:
       # is_student es true OR
       # is_senior es true OR
       # purchase_total >= 1000.0
       # Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.
   # Input:
       # purchase_total (float; total de la compra).
       # is_student_text (string; "YES" o "NO").
       # is_senior_text (string; "YES" o "NO").
   # Outputs: 
       # "Discount eligible:" true|false
       # "Final total:" <final_total>
   # Validations:
       # - purchase_total >= 0.0
       # - Normalizar is_student_text e is_senior_text a mayúsculas 
       # y convertir a booleanos is_student, is_senior.
       # - Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

# TEST CASES: 
     # Normal:
"""
Discount eligibility with booleans:

Total purchase: 1200
Are you a student? Yes
You are sir: No
Discount eligible: True
Final total:  1080.0
"""
     # Border:
"""
Discount eligibility with booleans:

Total purchase:1000
Are you a student?No
You are sir: No
Discount eligible: True
Final total:  900.0
"""
     # Error:
"""
Discount eligibility with booleans:

Total purchase: -100
Are you a student? Maybe
You are sir:No
ERROR: invalid input, please set an amount
"""

# CODE
print("\nDiscount eligibility with booleans: \n")

purschase_total = float(input("Total purchase:"))
is_student_text = input ("Are you a student?")
is_senior_text = input ("You are sir:")

is_student_text = is_student_text.upper().strip()
is_senior_text = is_senior_text.upper().strip()

if purschase_total <= 0.0: 
    print ("ERROR: invalid input, please set an amount ")
elif is_student_text not in ("YES","NO") and is_senior_text not in ("YES","NO"):
    print("Error: invalid input, please set 'YES' or 'NO'")
else: 
    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")
    discount_eligible = is_student or is_senior or (purschase_total >= 1000)

    if discount_eligible == True: 
        final_total = purschase_total * .9
    else: 
        final_total = purschase_total
    print (f"Discount eligible: {discount_eligible}" )
    print (f"Final total:  {final_total}")

# PROBLEM 4: Basic statistics of three integers 

   # Description:
       # Lee tres números enteros y calcula: suma, promedio (float), 
       # valor máximo, valor mínimo y un booleano all_even que indique 
       # si los tres números son pares.
   # Input:
       # n1 (int)
       # n2 (int)
       # n3 (int)
   # Outputs: 
       # "Sum:" <sum_value>
       # "Average:" <average_value>
       # "Max:" <max_value>
       # "Min:" <min_value>
       # "All even:" true|false
   # Validations:
       # - Verificar que los tres valores se puedan convertir a int.
       # - No se requieren restricciones adicionales (se permiten negativos).

# TEST CASES: 
     # Normal:
"""
Basic statistics of three integers:

Enter the first number: 4
Enter the second number: 6
Enter the third number: 8
Sum:18
Average:6.00
Max:8
Min:4
All even: True
"""
     # Border:
"""
Basic statistics of three integers:

Enter the first number: 3
Enter the second number: 5
Enter the third number: 7
Sum:15
Average:5.00
Max:7
Min:3
All even: False
"""
     # Error:
"""
Basic statistics of three integers:

Enter the first number: a
Enter numbers only
"""

# CODE
print ("\n Basic statistics of three integers: \n")
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))

    sum_value = n1 + n2 + n3
    average_value = (sum_value /3)
    max_value = max(n1,n2,n3)
    min_value = min(n1,n2,n3)
    all_even =(n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print(f"Sum:{sum_value}")
    print(f"Average:{average_value:.2f}")
    print (f"Max:{max_value}")
    print (f"Min:{min_value}")
    print (f"All even: {all_even}")
    
except ValueError: 
    print ("Enter numbers only")

# PROBLEM 5: Loan eligibility 

   # Description:
       # Determina si una persona es elegible para un préstamo con base en:
       # monthly_income (float)
       # monthly_debt (float)
       # credit_score (int)
       # La regla es:
         # debt_ratio = monthly_debt / monthly_income
         # eligible es true si:
         # monthly_income >= 8000.0 AND
         # debt_ratio <= 0.4 AND
         # credit_score >= 650
   # Input:
       # monthly_income (float; ingreso mensual).
       # monthly_debt (float; pagos mensuales de deuda).
       # credit_score (int; puntaje de crédito).
   # Outputs: 
       # - "Debt ratio:" <debt_ratio>
       # "Eligible:" true|false
   # Validations:
       # - monthly_income > 0.0 (evitar división entre cero).
       # - monthly_debt >= 0.0
       # - credit_score >= 0
       # - Si no se cumple, mostrar "Error: invalid input".

# TEST CASES: 
     # Normal:
"""
Loan eligibility:

Monthly income:10000
Monthly debt payments:3000
Credit score: 700
Debt ratio: 0.30
Eligible: True
"""
     # Border:
"""
Loan eligibility:

Monthly income:8000
Monthly debt payments:3200
Credit score: 650
Debt ratio: 0.40
Eligible: True
"""
     # Error:
"""
Loan eligibility:

Monthly income: 0
Monthly debt payments:3000
Credit score: 700
Error: Invalid input
"""

# CODE
print ("\nLoan eligibility: \n")
try:
    monthly_income = float(input("Monthly income:"))
    monthly_debt = float(input("Monthly debt payments:"))
    credit_score = int(input("Credit score:"))

    if monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income 
        eligible_person = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650

        print (f"Debt ratio: {debt_ratio:.2f}")
        print (f"Eligible: {eligible_person}")
    else: 
        print ("Error: Invalid input")

except ValueError: 
    print ("Error: Invalid input")
except KeyboardInterrupt: 
    print ("\n Process interrupted bu user")

# PROBLEM 6: Body Mass Index (BMI) and category flag

   # Description:
       # Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
       # bmi = weight_kg / (height_m * height_m)
       # Además, genera booleanos para indicar:
         # is_underweight (bmi < 18.5)
         # is_normal (18.5 <= bmi < 25.0)
         # is_overweight (bmi >= 25.0)
   # Input:
       # weight_kg (float; peso en kilogramos).
       # height_m (float; estatura en metros).
   # Outputs: 
       # "BMI:" <bmi_redondeado>
       # "Underweight:" true|false
       # "Normal:" true|false
       # "Overweight:" true|false
   # Validations:
       # - weight_kg > 0.0
       # - height_m > 0.0
       # - Si no se cumple, mostrar "Error: invalid input".

# TEST CASES: 
     # Normal:
"""
Body Mass Index (BMi):

Insert your weight in kg:70
Insert your height in meters:1.75
BMI: 22.86
Underweight: False
Normal weight: True
Overweightt: False
"""
     # Border:
"""
Body Mass Index (BMi):

Insert your weight in kg: 50
Insert your height in meters:1.70
BMI: 17.3
Underweight: True
Normal weight: False
Overweightt: False
"""
     # Error:
"""
Body Mass Index (BMi):

Insert your weight in kg: -50
Insert your height in meters: 1.70
Error: Invalid input
"""

# CODE
print ("\n Body Mass Index (BMi): \n")

try:
    weight_kg = float(input("Insert your weight in kg:"))
    height_m = float(input("Insert your height in meters:"))

    if weight_kg > 0.0 and height_m > 0.0: 
        bmi = weight_kg / (height_m ** 2)
        is_underweight = (bmi <18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print(f"BMI: {round(bmi,2)}")
        print (f"Underweight: {is_underweight}")
        print (f"Normal weight: {is_normal}")
        print (f"Overweightt: {is_overweight}")
    else: 
        print ("Error: Invalid input")
except ValueError:
    print ("Error: Invalid input")
except KeyboardInterrupt:
    print ("Process interrupted by user")

# CONCLUSIÓN:
"""
    Los enteros (int) y los flotantes (float) son esenciales para realizar cálculos reales, 
    especialmente cuando se combinan. Los enteros se usan típicamente para contar elementos 
    discretos, como horas trabajadas, mientras que los flotantes se usan para representar 
    valores continuos como salarios o temperaturas. Juntos, permiten realizar cálculos 
    más completos y precisos, como en el caso de las horas extras o la relación de deuda.

    Las comparaciones entre valores generan booleanos (True o False), los cuales son fundamentales 
    para la toma de decisiones. Usar sentencias `if` basadas en estas comparaciones permite que 
    el programa ejecute diferentes acciones dependiendo de si la condición es verdadera o falsa. 
    Este mecanismo es esencial para validar rangos y tomar decisiones dinámicas.

    Estos patrones se repiten en problemas comunes como nómina, descuentos, préstamos y más, 
    donde es necesario realizar cálculos basados en múltiples condiciones y validar entradas 
    antes de procesar la información para evitar errores y garantizar resultados correctos.
"""
# REFERENCIAS:

# 1) Built-in types. (s/f). Python Documentation. Recuperado el 
 # 2 de diciembre de 2025, de https://docs.python.org/3/library/stdtypes.html
# 2) 📗 Boolean Python. (s/f). El Libro De Python. 
 # Recuperado el 2 de diciembre de 2025, de https://ellibrodepython.com/booleano-python
# 3) Operadores en Python: Guía completa [Aritméticos, Lógicos y más]. (2025, octubre 19). El
 # Pythonista. https://elpythonista.com/operadores-en-python-guia-completa-2025-aritmeticos-logicos-y-mas
# 4) Young, L. (2024, agosto 12). Operatores en Python – Lógica, Aritmética, 
 # Comparación. Guru99. https://www.guru99.com/es/python-operators-complete-tutorial.html
# 5) Data types — NumPy v2.3 manual. (s/f). Numpy.org. 
 # Recuperado el 2 de diciembre de 2025, de https://numpy.org/doc/stable/user/basics.types.html


