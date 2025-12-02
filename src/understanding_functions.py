
"""
    Functions: 
    
        Las funciones son bloques de código diseñados
        para realizar un tarea especifica. 

        Cuando queremos realizar la tarea que se ha definido 
        en una función, tenemos que llenar el nombre 
        de la funcion responsable a esto. 

        Definición de una función (Syntax):

            def name_of_function(parameters)
                actions
"""

def greet_mauro ():
    print ("Hola Mauro, que gusto verte")

# Parametros 
def greet(username, msj): 
    print (f"Hola {username}, {msj}")

# Argumentos 
# greet_mauro()
# greet("Andres", "Se te pegaron las cobijas")

"""
    Vamos a realizar un programa que genere
    el nombre completo de una persona.

    Vamos a pasarle primer nombre, el segundo 
    y el apellido.

    La función debe generar el nombre completo 
    y regresarlo

"""
def creat_full_name(first_name, last_name, middle_name=""):
    """
        Docstrings - This function cretaes the fullname
        of a person given its three names. 
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escibre tu segundo nombre: ").strip().lower()
user_last_name = input("Escribre tus apellidos: ").strip().lower()

# Argumentos Posicionales -> Pisitiomal Arguments

print(creat_full_name(
    user_first_name, 
    user_last_name,
    user_middle_name))

# Argumentos Claves -> Keyword Arguments 
full_name_key = creat_full_name ( 
    last_name = user_last_name,
    first_name = user_first_name,
    middle_name = user_middle_name)

print (full_name_key)
   
# Parametros opcionales 

profe_falso = creat_full_name(user_first_name, user_last_name)
print (profe_falso)

# Temas para estudiar a futuro 
# args, kwargs -> En funciones 
# manejo de datos: csv, jsom. .yml, .txt, .xls, .doc
# argumentos por línea de comandos - sys
# cli - command line interface
# testing ->
