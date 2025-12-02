
# Poblema 1 Palindrome checker 


phrase = input("Ingresa la frase: ")
phrase = phrase.strip()

if len(phrase) >= 3: 
    clean_phrase = phrase.lower().replace(" ", "")
    is_palindrome = clean_phrase[::-1]

    if clean_phrase == is_palindrome:
        print("Is palindrome: TRUE")
    else: 
        print("Is palindrome: FALSE")
else:
     print("Ingresa al menos 3 caracteres")

# Problem 2 Works hours and overtime payment 
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
     
# Preguntas de rescate 
# Menciona al menos de dos diferencias entre listas y tuplas, 
# y explica cuando conviene usar cada una.
"""
    Listas:
        1: Son mutables, lo que permite agregar una mayor cantidad de 
        "objetos", dentro la lista
        2: Estas poseen un espacio de almacenamiento más amplio que una 
        tupla, ya que de manera constante se pueden ir agregando mas cosas.
    Tupla_
        1: Son inmutables, lo que los hace tener un rango definido, y no 
        puede ser modificado.
        2. Al ser inmutables, estas poseen un rango de almanecamiento fijo.
"""
# Explica la diferencia entre un ciclo for y un ciclo While

"""
    For: Este son para ciclos finitos, los cuales tienen a un inicio y
    un final, un ejemplo para su utilización es para poder imprimir 
    una lista.

    While: Utilizado para ciclos infinitos, que pueden repertirse de 
    manera constante, un ejemplo de esto, es cuando NO cumplimos la funcion d
    del While, este se repite, un ejemplo de esto es cuando lo utilizamos para
    alguna aplicación de algun banco.
"""
# Funciones en un programa. 
"""
    Legibilidad: Hace que nuestro codigo, pueda tener una
    vista mas simple y agradable, al usuario o al que la programe
    o utilizar pruebas como .upper.title, que normaliza las strings 
    a la hora de ser impresas en el codigo.  

    Reutilización: Podemos reutilizar una misma variable y 
    emplearle nuevas funciones, al tener ciertas modificaciones 
    lo que me permite tener una constante actualizacion en nuestro 
    programa. 

    Pruebas: Nos permite reconocer determinados errores, que podemos 
    tener en nuestro codigo, y poder corregirlos de manera exitosa.
    como el print, o los value error.
"""