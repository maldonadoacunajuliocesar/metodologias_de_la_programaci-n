
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