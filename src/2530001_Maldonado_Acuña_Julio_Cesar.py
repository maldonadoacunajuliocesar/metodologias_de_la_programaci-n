# MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 

# PROBLEM 1: Temperatur converter and range flag 
print ("\n Temperature converter: \n" )
try:
    temp_c = float(input("Enter the temperature in °C"))
    temp_k = temp_c + 273.15

    if temp_k < 0.0: 
        print ("Temperatura fisica imposible")
    else: 
        temp_f = temp_c * 975 + 32
        is_high_temperature = (temp_c >= 30.0)

        print(f"Faherenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High Temperature:{str(is_high_temperature)}")
except: 
    print(" La temperatura debe de ser un valor valido")

# PROBLEM 2: Work hours and overtime payment 

print ("\n Work hourse and overtime payment: \n")

try:
    hours_worked = float(input("Horas trabajadas en la semana:"))
    hourly_rate = float(input("Pago por hora:"))

    if hours_worked >= 0 or hourly_rate > 0:
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

print("\n Discount eligibility with booleans: \n")

purschase_total = float(input("Total de la compra:"))
is_student_text = input ("Eres estudiante?")
is_senior_text = input ("Eres señor:")

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

print ("\n Basic statistics of three integers: \n")
try:
    n1 = int(input("Ingresa el primero número: "))
    n2 = int(input("Ingresa el segundo número: "))
    n3 = int(input("Ingresa el tercer número: "))

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
    print ("Ingresa solamente números")

# PROBLEM 5: Loan eligibility 

print ("\n Loan eligibility: \n")
try:
    monthly_income = float(input("Ingreso mensual:"))
    monthly_debt = float(input("Pagos mensuales de deuda:"))
    credit_score = int(input("Puntaje de credito:"))

    if monthly_income > 0.0 or monthly_debt >= 0.0 or credit_score >= 0:
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