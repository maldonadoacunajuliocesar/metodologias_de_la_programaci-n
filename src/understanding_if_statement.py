
# IF 

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars: 
    if car == "bmw": 
        print (car.upper())
    else: 
        print (car)

# El condicional es el corazón de un if 

# Condicional 
car = "bwm"
print (car== "bwm") # True 

# Condicionl Fase 
car = "Audi"
print (car == "audi")

# Posible Solución a entradas del usuario 
car = "Audi"
print (car.lower() == "audi") # True

# Operador relacional != para determinar desigualdad 
requested_topping = "Mushroom"
if requested_topping != "Anchovies": # True
    print ("Hold the anchovies")

# Compraciones numéricas 
age = 18   # Entero 
print (age == 18) # True 

answer = 17 
if answer != 42:
    print ("\n Esa no es la respuesta correcta")

age = 17 
print (age < 21) # True 
print (age <= 21) # True
print (age > 21) # False
print (age >= 21) # False 

# Multiples condiciones 
age_0 = 22 
age_1 = 18 
# And 
print (age_0 >= 21 and age_1 >= 21) # False 
print (age_0 >= 21 and age_1 >= 18) # True 

# Or 
print (age_0 >= 21 or age_1 >= 21) # True
print (age_0 >= 21 or age_1 >= 21) # False

"""
    Para preguntarnos si un valor especpifico 
    está en una lista, podemos utilizar el siguiente
    comparador: 

    value in list
"""
motorcycles= ["mortalica", "honda", "vento", "yamaha"]
moto_charly_wants = "italica"
print (moto_charly_wants in motorcycles) # False 
print ("honda" in motorcycles) # True 

"""
    Para preguntarnos si un valor especifico
    NO está en una lista, podemos utilizar el
    siguient comparador: 

    value not in list
"""

banned_students = ["jorge", "carlos", "moyra", "gus", "hots"]
user = "mauro"
print (user not in banned_students) # True 
print ("jorge" not in banned_students) # False

# Variables del tipo booleano 
game_activate = True 
can_edit = False 

# If stament 

"""
    Sintax: 
    
    if condition: 
        do something 


    if condition: 
        do something 
    else: 
        do something
    
"""
# Actividad 

age = int(input("\n ¿Dime cuál es tu edad? "))
print (age)

if age >= 18: 
    print ("Tu tienes la edad suficiente para votar")
else: 
    print ("Tu eres menor de edad")


