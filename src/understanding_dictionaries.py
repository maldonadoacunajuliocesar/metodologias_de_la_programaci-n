
# Simple dictionary 
alien_0 ={"Color": "green", "points": 5}

# Diccionario simple 
alien_1 = {"color": "yellow"}

# Acceidnedo a valores en diccionario 
print (alien_1 ["color"])
print (alien_0["points"])

# Diccionario Vacio 
alien_2 = {}

# Modificando valores en un diccionario 
alien_2 = {"color": "yellow"}
alien_2 ["color"] = "blue"
print (alien_2)

# Adding values in a dictionary 
alien_2 ["x_position"] = 0 
alien_2 ["y_position"] = 25 

print (alien_2)

# Dictionary to store similar objects 
print ("\n DICCIONARIO: \n")
favorite_languajes = {
    "jen": "python", 
    "sarah": "c", 
    "edward": "ruby",
    "phill": "python"
    }

for key, value in favorite_languajes.items(): 
    print (f"{key.title()}'s favorite \
language is {value.title()}.")

# Looping para llaves
print("\n IMPRIMIR LLAVES: \n")
for key in favorite_languajes.keys():
    print (key)

# Looping por valores 
print ("\n IMPRIMIR VALORES: \n")
for value in favorite_languajes.values(): 
    print (value)

# TAREA -  Investigar el nesting diccionario 
# Listas de diccionarios 
# Listas en diccionarios 
# Diccionarios en diccionarios 
