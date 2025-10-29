
# Practica 1 

message = "This is my first variable in Python"
another_message = 'Variables are used to store information'

print(message)
print(another_message)

print (message, another_message, message)

"""

Los nombres de variables en Python deben nombrarse solo con: 

    - Letras, números y guión bajo (espacios)
    - Deben comenzar con una letra o con guión bajo, pero No con npumero:
        ejemplo correcto: message_1 
        ejemplo incorrecto: 1_message 
    - No utilizar espacios para separar palabras en los nombres de las variables 
    - No utilizar palabras reservadas de Python para nombrar variables o archivos
    - Los nombres deben de ser cortos, pero descriptivos
    - Los nombres deben de ser en inglés 
    - Nombres de las variables en minúsculas 

"""

charly_message = "Hola, Soy Charly y estoy aprendiendo Python! "
print(charly_message)
print(charly_message)

"""""
Tracebak: Es un registro de donde el interprete 
         tuvo problemas para ejecutar el código.
   Ejemplo: 
   Traceback (most recent call last):
    File "C:\Users\julio\Proyects\metodologias_de_la_programaci-n\src\understanding_variables.py", line 30, in <module>
    print(charly_mesage)
          ^^^^^^^^^^^^^
   NameError: name 'charly_mesage' is not defined. Did you mean: 'charly_message'?

NameError: Signigica que olvidamos establecr el valor de una variable
       antes de utilizar o cometimos un error al ingresar el nombre de la variable.

"""""