
# Practica 2 Strings

"""
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples 
    '' o dobles "" es considerado un string. 
    
     "Esto es un string"
     'Esto también es un string' 

     'Le dije aun amigo, "Python es mi lenguaje favorit!"'
     "El lenguaje 'Python' lleva el nombre por Monty Pythom, 
     no por la serpiente."

"""
name = "Clase de programación"
print (name)
print (name.title())
print (name)

"""
   Un método es una acción que python puede realizar 
   en un fragmento de datos o sobre una variable. 

   El punto. después de una variable seguida del método title () 
   dice que se tiene que ejecutar el método title () en la variable name.

   Todos los métodos van seguidor de paréntesis porque 
   en ocasiones necesitan información adicional para funcionar,
   lo cual iría dentro de los paréntesis.

   En esta ocasión el método title() no necesita información adicional
   para ejecutarse.

"""
print (name.upper())
print (name.lower())

# Practica 3 Concatenación de Strings

print("Concatenación de strings")
first_name = "Charly"
last_name = "Mercury"

fullname = first_name + " " + last_name
print(fullname)

print ("Hola, " + fullname.title() + "!")
print ("Hola, " + fullname.upper() + "!")

# Practica 4 Syntax Error con Strings 

message =  "Una fortaleza de Python es su comunidad" 
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message) 

# Practica 5 Concatenación convencional 

famous_person = "Charly Mercury"
quote = "Pyhton is love"

message = famous_person + " una vez dijo " + quote
print(message)

# Practica 6 Concatenación con f-strings

"""
 () - Se llaman Paréntesis 
 {} - Se llaman Llaves 
 [] - Se llaman Corchetes
"""
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string) 

# Actividad 

"""
 1) Elige un persibaje famoso e igualalo a una varaible tipo string 
 2) Elige una frase famosa que haya dicho e igulalo a una variable tipo string
 3) Genera un mensaje con las dos varianles utilizando f-string 
 4) Imprime el mensaje 
"""

famous_person1 = "Nelson Mandela "
quote1 = "La educación es el arma más poderosa que puedes usar para cambiar el mundo"

message_1 = f"{famous_person1} una ves dijo {quote1}"
print(message_1)

# Practica 7 Whitespace 
"""
Whitespace se refiere a cualquier caracter que no se imprime, es decir, un tabulador y finales de línea. Los whitespaces
se utilizam comúnmente para organizar las salidad (prints) de tal manera que sea más amigable de leer o ver para los usuarios.
"""
# Ejemplos 
print("Python")
print("\tPython")  

# Ejemplos Salto de línea
print ("Languages: \n Python \n C \n JavaScript")

# Eliminación de espacios en blanco 
progrmamming_language = "   Python   "
print(progrmamming_language)
print(progrmamming_language.lstrip())  
print(progrmamming_language.rstrip())
print(progrmamming_language.strip())

progrmamming_language = "   Python Javascrip "
print(progrmamming_language)
print(progrmamming_language.lstrip())  
print(progrmamming_language.rstrip())
print(progrmamming_language.strip())

