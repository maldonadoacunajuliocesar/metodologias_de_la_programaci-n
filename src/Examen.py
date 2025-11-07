
# TEMAS VISTOS EN CLASE ;)

    # Tema 1 - Variables en Python

message = "Hi, this is my first variable in Python"
another_message = "Variables are used to store information"

print (message)
print (another_message)

print (message, another_message, message) # Imprimir varias variables en una sola línea

    # Tema 2 -Strings en Pyhton 

name = "Clases de programación"
print (name)

print (name.title()) # Primera letra en mayúscula
print (name.upper()) # Todo en mayúscula
print (name.lower()) # Todo en minúscula 

    # Tema 2.1 Concatenación Convencional de Strings 

first_name = "Julio"
last_name = "César"

full_name = first_name + " " + last_name 
print (full_name)

print ("Hola," + full_name.title() + "!")
print ("Hola," + full_name.upper() + "!")
print ("Hola," + full_name.lower() + "!")

    # Tema 2.2 Concatenación con f-strings

famous_person = "Julio César"
qoute = "Soy la Cabra" 

message_f_string = f"{famous_person} una vez dijo {qoute}"
print (message_f_string)

    # Tema 2.3 Actividad de Strings 

famous_person1 = "Albert Einstein"
qoute1 = "Yo solo se que no se nada"

message_f_string1 = f"{famous_person1} una vez dijo {qoute1}"
print (message_f_string1)

    # Tema 2.4 Whitespace en Strings

print ("Python")  # Normal 
print ("\t Python") # Agrega una tabulación antes de la palabra Python
print ("Languages: \n Python ") # Agrega un salto de línea antes de la palabra Python

    # Tema 2.4.1 Eliminación de Whitespace en Strings

programing_language = " Python "

print (programing_language)
print (programing_language.lstrip()) # Elimina espacios en blanco a la izquierda
print (programing_language.rstrip()) # Elimina espacios en blanco a la derecha
print (programing_language.strip()) # Elimina espacios en blanco a ambos lados

    # Tema 3 - Números en Python 

number_1 = 39 
number_2 = 13 

sum = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2
quotient = number_1 / number_2 
modulo = number_1 % number_2
power = number_1 ** 2

print ("Suma:", sum)
print ("Diferencia:", difference)
print ("Producto:", product)
print ("Cociente:", quotient)
print ("Modulo:", modulo )
print ("Potencia:", power)

    # Tema 3.1 Uso de type () 

print (type(sum)) # Imprime el tipo de dato de la variable sum
print (type(quotient)) # Imprime el tipo de dato de la variable quotient

    # Tema 3.2 Conversión de Tipos de Datos

        # Utilizar la función str() para convertir números en strings
age = 35 
message = "Julio tiene " + str(age) + " años."
print (message)

        # Utilizar la función f strings para evitar la conversión 
message_f = f"Charly tiene {age} años"
print (message_f)

    # Tema 4 - Listas en Python

fruits = ["apple", "banana", "cherry", "watermelon"]
print (fruits)

print (fruits[0]) # Acceder al primer elemento "apple"
print (fruits[1]) # Acceder al segundo elemento "banana"
print (fruits[2]) # Acceder al tercer elemento "cherry"
print (fruits[3]) # Acceder al cuarto elemento "watermelon"

    # Tema 4.1 Listas - Strings - Metodos

print (fruits[0].upper())
print (fruits[1].title())
print (fruits[2].lower())

    # Tema 4.2 Ultimo elemento de una lista 

print (fruits [-1])
print (fruits [-2])
print (fruits [-3])

# PREGUNTA DE EXAMEN ¿PORQUE UNA LISTA ES MUTABLE? Porque podemos cambiar sus elementos después de haberla creado.

    #  Repasando lo visto 

message = f"Mi fruta favorita {fruits[3].title()}"
print (message)

    # Tema 4.3 Agregar elementos a una lista

      # append(): Agrega un elemento al final de la lista.
print ("\n Agregar elemento a una lista: Metodo append() \n")
motorcycles = ["Honda", "Yamaha", "Suzuki", "BMW"]
print (motorcycles)
motorcycles.append ("Ducati")
print (motorcycles)

        # insert(): Inserta un elemento en una posición específica de la lista.
print ("\n Agregar elemento a una lista: Metodo insert() \n ")
motorcycles = ["Honda", "Yamaha", "Suzuki", "BMW"]
print (motorcycles)
motorcycles.insert (0, "Ducati")
print (motorcycles)
print (motorcycles[0])  

    # Tema 4.4 Eliminar elementos de una lista

print( "\n Eliminar elementos de una lista: Metodo 'del' \n")
motorcycles = ["Honda", "Yamaha", "Suzuki", "BMW"]
print (motorcycles) 
del motorcycles[0]
print (motorcycles)

