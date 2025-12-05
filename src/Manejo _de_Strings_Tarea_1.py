
# MANEJO DE STRINGS EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 
     
"""
    1. ¿Qué es un string en Python? 
        Un string en Python es un tipo de dato que representa texto. 
        Son inmutables: no se pueden modificar directamente; cualquier cambio 
        crea una nueva cadena.  

    2. ¿Qué operaciones básicas se pueden realizar?
        Con strings se pueden hacer operaciones básicas como concatenar textos, 
        obtener su longitud con len(), extraer subcadenas con slicing, buscar 
        patrones con find() o in, y reemplazar texto con replace().

    3. ¿Por qué es importante validar y normalizar texto de 
    entrada?
        Es importante validar y normalizar el texto de entrada (como correos, nombres 
        o contraseñas) para evitar errores, datos inválidos o inconsistencias.

    4. ¿Qué cubrirá tu documento?
        Este documento cubre la descripción de cada problema, entradas, salidas, 
        validaciones aplicadas y el uso de métodos de string acompañado de casos 
        de prueba ejecutables dentro del script.
"""
# PRINCIPIOS Y BUENAS PRÁCTICAS:
"""
    1. Los strings son inmutables: cualquier operación crea una nueva cadena.
    2. Es buena práctica normalizar entradas con strip() y lower() antes de comparar.
    3. Evitar "números mágicos" en índices; documentar qué hace cada slice.
    4. Usar métodos de string integrados antes de reescribir lógica manual.
    5. Diseñar validaciones claras: primero que no esté vacío, luego el formato.
    6. Escribir código legible: nombres de variables descriptivos y mensajes de error útiles.
"""

# PROBLEM 1: Full Name Formatter (name + initials)

   # Description:
       # Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
       # 1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
       # 2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
   # Inputs: 
       # full_name
   # Outputs: 
       # (f"Formmatted name: {full_name_1.title()} ")
       # (f"Initials: {initials}")
   # Validations:
       # full_name no debe estar vacío después de strip().
       # Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
       # No aceptar cadenas que sean solo espacios.

# TEST CASES: 
     # Normal: 
"""
Full Name Formatter:

Enter your full name:juan carlos tovar
Formatted name: Juan Carlos Tovar
Initials: J.C.T
"""
     # Border:
"""
Full Name Formatter:

Enter your full name:    luis   lopez
Formatted name: Luis   Lopez
Initials: L.L
"""
     # Error:
"""
Enter your full name:julian
Formatted name: Julian
Initials: J
"""

# CODE 
print ("\n Full Name Formatter: \n")

full_name = input("Enter your full name:")

full_name_1 = full_name.strip()

if len(full_name_1) == 0: 
    print ("You didn't enter any name.")
elif len(full_name_1) < 2:
    print ("Please enter at least a first and last name.")
else: 
    words = full_name_1.split()
    initials = ".".join([word[0].upper() for word in words])
    print (f"Formatted name: {full_name_1.title()}")
    print (f"Initials: {initials}")

# PROBLEM 2: Simple Email Validator (structure + domain)

    # Description:
       # Valida si una dirección de correo tiene un formato básico correcto:
       # Contiene exactamente un '@'.
       # Después del '@' debe haber al menos un '.'.
       # No contiene espacios en blanco.
       # Si el correo es válido, también muestra el dominio (la parte después de '@').
   # Inputs:
       # email_text
   # Outputs: 
       # Valid email: True")
          # print (f"Domain: {domain}"
       # Valid email: False
   # Validations:
       # email_text no vacío tras strip().
       # Contar cuántas veces aparece '@'.
       # Verificar que no haya espacios (no debe haber " " en email_text).

# TEST CASES: 
     # Normal:
"""
Simple Email Validador:

Enter your email: julio@gmail.com
Valid email: True
Domain: gmail.com
"""
     # Border:
"""
Simple Email Validador:

Enter your email: maria@correo
Valid email: False
"""
     # Error:
"""
Simple Email Validador:

Enter your email:
You didn't enter any email address.
"""

# CODE
print ("\n Simple Email Validador: \n")

email_text = input ("Enter your email: ")
email_text = email_text.strip()

if len(email_text) == 0: 
    print ("You didn't enter any email address.")
elif email_text.count ("@") != 1:
    print ("Invalid email. It must contain an @.")
elif " " in email_text: 
    print ("Invalid email. It must not contain spaces.")
else: 
    at_index = email_text.find ("@")
    domain = email_text [at_index + 1:]

    if "." in domain:
        print ("Valid email: True")
        print (f"Domain: {domain}")
    else: 
        print ("Valid email: False")

# PROBLEM 3: Palindrome Checker 
   # Description:
       # Determina si una frase es un palíndromo, es decir, 
       # se lee igual de izquierda a derecha y de derecha a izquierda, 
       # ignorando espacios y mayúsculas/minúsculas.
   # Inputs: 
       # phrase (string).
   # Outputs:
       #  "Is palindrome: true" o "Is palindrome: false"
   # Validations:
       #  phrase no vacía tras strip().
       #  Longitud mínima razonable después de limpiar espacios 
       #  (por ejemplo, al menos 3 caracteres).

# Test cases: 
     # Normal:
"""
Palindrome Checker:

Please enter a sentence: Anita lava la tina
Is palindrome: True
"""
     # Border:
"""
Palindrome Checker:

Please enter a sentence: hello
Is palindomre: False
"""
     # Error:
"""
Palindrome Checker:

Please enter a sentence:
Enter a phrase of three or more characters
"""

# CODE
print ("\nPalindrome Checker: \n")

phrase = input("Please enter a sentence: ")
phrase = phrase.strip()

if len(phrase) == 0 or len(phrase) < 3: 
    print ("Enter a phrase of three or more characters")
else: 
    clean_phrase = phrase.lower().replace (" ", "")
    reversed_phrase = clean_phrase[::-1]

    if clean_phrase == reversed_phrase: 
        print ("Is palindrome: True" )
    else: 
        print ("Is palindomre: False")

# PROBLEM 4:  Sentence Word Stats (lengths and first/last word)
   # Description: 
       # 1) Normalizar espacios (quitar espacios al principio y al final).
       # 2) Separar las palabras por espacios.
       # 3) Mostrar:
          # - Número total de palabras.
          # - Primera palabra.
          # - Última palabra.
          # - Palabra más corta y más larga (por longitud).
   # Inputs: 
       # - sentence (string).
   # Outputs:
       # - "Word count: <n>"
       # - "First word: <...>"
       # - "Last word: <...>"
       # - "Shortest word: <...>"
       # - "Longest word: <...>"
   # Validations
       # - Oración no vacía tras strip().
       # - Debe contener al menos una palabra válida después de split().

# Test cases: 
     # Normal:
"""
Sentence Word Stats:

Enter a sentence: The quick brown fox
Word count: 4
First word: The
Last word: fox
Shortest word: The
Longest word: quick
"""
     # Border:
"""
Sentence Word Stats:

Enter a sentence: hello
Word count: 1
First word: hello
Last word: hello
Shortest word: hello
Longest word: hello
"""
     # Error:
"""
Sentence Word Stats:

Enter a sentence:
Enter a correct sentence
"""

# CODE
print ("\nSentence Word Stats: \n")

sentence = input("Enter a sentence:")
sentence = sentence.strip()
 
if len(sentence) == 0: 
    print ("Enter a correct sentence")
else: 
    space_sentence = sentence.split()

    if len(space_sentence) == 0:
        print ("It must contain at least one word")
    else: 
        longth_word = len(space_sentence)
        first_word = space_sentence[0]
        last_word = space_sentence[-1]
        shortest_word = min(space_sentence, key=len)
        longest_word = max(space_sentence, key=len)

        print (f"Word count: {longth_word}")
        print (f"First word: {first_word}")
        print (f"Last word: {last_word}")
        print (f"Shortest word: {shortest_word}")
        print (f"Longest word: {longest_word}")

# PROBLEM 5: Password strength classifier 
   # Description:
       # Clasifica una contraseña como "weak", "medium" o "strong" según reglas 
       # mínimas (puedes afinarlas, pero documéntalas en los comentarios).
   # Inputs: 
       # - password_input (string).
   # Outputs:
       # - "Password strength: weak"
       # - "Password strength: medium"
       # - "Password strength: strong"
   # Validations:
       # - No aceptar contraseña vacía.
       # - Verificar longitud con len().

# Test cases: 
     # Normal:
"""
Password strength classifier:

Enter your new password: password123
Password strenght: Medium
"""
     # Border:
"""
Password strength classifier:

Enter your new password: 12345
Password strength: Weak
"""
     # Error:
"""
Password strength classifier:

Enter your new password:
The password cannot be empty
"""

# CODE
print ("\n Password strength classifier: \n")

password_input = input ("Enter your new password:")
password_input = password_input.strip()

if len(password_input) == 0: 
    print ("The password cannot be empty")
else:
    has_upper = False 
    has_lower = False
    has_digit = False
    has_symbol = False

    for word in password_input: 
        if word.isupper():
            has_upper = True
        elif word.islower():
            has_lower = True 
        elif word.isdigit(): 
            has_digit = True 
        elif not word.isalnum(): 
            has_symbol = True 

    length = len(password_input)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print ("Password strenght: Strong")
    elif length >= 8 and (has_upper or has_lower) and has_digit: 
        print ("Password strenght: Medium")
    else: 
        print ("Password strength: Weak")

# PROBLEM 6: Product label formatter (fixed-width text)
   # Description:
       # Dado el nombre de un producto y su precio, genera una etiqueta 
       # en una sola línea con el siguiente formato:
       # Product: <NAME> | Price: $<PRICE>
       # La cadena completa debe tener exactamente 30 caracteres:
         # - Si es más corta, rellena con espacios al final.
         # - Si es más larga, recorta hasta 30 caracteres.
   # Inputs: 
       # - product_name (string).
       # - price_value  (Int)
   # Outputs:
       # - "Label: <exactly 30 characters>"
   # Validations:
       # - product_name no vacío tras strip().
       # - price_value debe poder convertirse a un número positivo.

# Test cases: 
     # Normal:
"""
Product label formatter:

Enter the product name: Laptop
Enter the product price: 999.99
Product: Laptop| Price: $999.9
"""
     # Border:
"""
Product label formatter:

Enter the product name: Phone
Enter the product price: 50
Product: Phone| Price: $50.0
"""
     # Error:
"""
Product label formatter:

Enter the product name:
The product name cannot be empty
"""

# CODE
print ("\nProduct label formatter: \n")

product_name = input("Enter the product name:")

product_name = product_name.strip()

if len(product_name) == 0: 
    print ("The product name cannot be empty")
else: 
    try:
        price_value = float(input("Enter the product price:"))
        if price_value < 0:
            print ("The price cannot be negative.")
        else: 
            product = (f"Product: {product_name}| Price: ${price_value}")
        if len(product) < 30:
            product = product + ( " " * (30 - len(product)))
            print(product)
        else: 
            product = product[:30]
            print (product)
    except:
        print ("The price must be a valid number.")

# CONCLUSIONES:
"""
    El manejo de cadenas de texto es esencial en la entrada y salida de datos, ya que la mayoría  de las 
    interacciones con el usuario, como el ingreso de información o la visualización de resultados, 
    se realizan a través de cadenas. Funciones como `lower()`, `strip()`, `split()` y `join()` son clave 
    para garantizar que los datos sean procesados de manera consistente, especialmente cuando se trata 
    de entradas del usuario, donde el formato puede variar. Usar `lower()` o `strip()` asegura que 
    diferencias en mayúsculas o espacios adicionales no interfieran con las comparaciones, mientras que 
    `split()` y `join()` facilitan la manipulación del texto al procesarlo y mostrarlo de manera estructurada.

    A través de este ejercicio, aprendí que las cadenas en Python son inmutables, lo que significa que 
    cuando cambiamos una cadena, en realidad estamos creando una nueva. Esto es importante porque las operaciones 
    como el slicing o la concatenación de cadenas crean nuevos objetos de cadena en lugar de modificar la original.

    Finalmente, el uso de slices es una característica poderosa de Python, ya que permite acceder fácilmente a 
    partes específicas de una cadena, facilitando la manipulación de texto sin necesidad de bucles o índices complejos.
"""
# REFERENCIAS:

# 1) string — Common string operations. (s/f). Python Documentation. 
  # Recuperado el 2 de diciembre de 2025, de https://docs.python.org/3/library/string.html
# 2) Python strings. (s/f). W3schools.com. 
  # Recuperado el 2 de diciembre de 2025, de https://www.w3schools.com/python/python_strings.asp
# 3) (S/f). Datacamp.com. Recuperado el 2 de diciembre de 2025, 
  # de https://www.datacamp.com/tutorial/python-user-input
# 4) Python, R. (2024, diciembre 22). Strings and character data in python. Realpython.com; 
  # Real Python. https://realpython.com/python-strings/
# 5) Python string methods. (s/f). W3schools.com. 
  # Recuperado el 2 de diciembre de 2025, de https://www.w3schools.com/python/python_ref_string.asp