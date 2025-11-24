 
    # Actividad de Tarea 

"""
    Hacer un programa que pregunte la edad de una persona 
    y responda lo siguiente: 

      - Si la edad es menor e igual a 4, entonces la entrada 
       es gratuita
      - Si la edad es menor e igual a 18, pero mayor que
      4 entonces la entrada cuesta $200
      - Si la edad es mayor que 18, entonces la entrada cuesta 400
""" 
try:
    age = int(input("Ingresa tu edad por favor."))
except:
    age = -1 
    print ("Ingresa un valor númerico válido")

if age <= 4 and age >= 0: 
    print ("Tu entrada es gratuita")
elif age < 18 and age > 4: 
    print ("Tu entrada cuesta $200")
elif age >= 18: 
    print ("Tu entrada cuesta $400")
else:
    print ("Tuviste un error al ingresar tu edad")





