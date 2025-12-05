# MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 

"""
    1. ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
        Lista: Es una colección ordenada y mutable de elementos. Puedes modificar, 
        agregar o eliminar elementos en una lista después de haberla creado. 
        Se define usando corchetes [], por ejemplo: mi_lista = [1, 2, 3].

        Tupla: Es una colección ordenada, pero inmutable, lo que significa que una 
        vez creada no puedes modificar sus elementos. Se define usando paréntesis (), 
        por ejemplo: mi_tupla = (1, 2, 3).

        Diccionario: Es una colección no ordenada que asocia claves con valores. 
        Cada elemento se representa como un par clave-valor, y se define usando llaves {}, 
        por ejemplo: mi_diccionario = {"a": 1, "b": 2}.

        Diferencias:
        Las listas y tuplas son ordenadas, pero las listas son mutables (puedes 
        cambiar sus elementos) y las tuplas no (son inmutables).

        Los diccionarios son no ordenados (aunque en versiones más recientes de 
        Python mantienen el orden de inserción) y permiten almacenar pares clave-valor, 
        lo que no es posible en listas o tuplas.

    2. ¿Qué significa que una lista sea mutable y una tupla inmutable?
        Mutable (Lista): Significa que puedes cambiar los valores dentro de la 
        lista después de haberla creado. Puedes agregar, eliminar o modificar los elementos. 
        Ejemplo: mi_lista[0] = 10 cambiaría el primer elemento de la lista.

        Inmutable (Tupla): Significa que una vez que la tupla se ha creado, 
        no puedes cambiar, agregar o eliminar elementos de ella. Ejemplo: mi_tupla[0] = 10 
        generaría un error porque las tuplas no permiten modificaciones.

    3. ¿Cómo se usan los diccionarios para asociar claves con valores?
        En un diccionario, cada clave se asocia a un valor específico. 
        Puedes acceder a los valores a través de sus claves. Las claves deben ser únicas y,
        generalmente, son de tipos inmutables como cadenas o números, 
        mientras que los valores pueden ser de cualquier tipo.

    4. ¿Qué cubrirá tu documento?
        El documento incluirá una descripción de cada problema, especificando cómo se usan 
        las listas, tuplas y diccionarios en diferentes contextos prácticos, como catálogos,
        registros y estadísticas. Se detallarán las entradas y salidas de cada problema, las 
        validaciones necesarias y cómo cada estructura de datos contribuye a resolver cada tarea,
        como almacenar y acceder a información de manera eficiente.
"""

# PRINCIPIOS Y BUENAS PRÁCTICAS 
"""
    1. Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
    2. Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
    3. Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
    4. Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
    5. Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
    6. Escribir código legible y mensajes claros para el usuario.
"""
# PROBLEM 1: Shopping list basics (list operations)

   # Description:
       # Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
         # 1) Crear una lista inicial de productos.
         # 2) Permitir agregar un nuevo producto al final.
         # 3) Mostrar la cantidad total de elementos en la lista.
         # 4) Verificar si un producto específico está en la lista (booleano is_in_list).
   # Inputs: 
       # initial_items_text (string; por ejemplo, "apple,banana,orange").
       # new_item (string; producto a agregar).
       # search_item (string; producto a buscar).
   # Outputs: 
       #  "Items list:" <items_list>
       # "Total items:" <len_list>
       # "Found item:" true|false
   # Validations:
       # - initial_items_text no vacío tras strip().
       # - Separar la cadena por comas y eliminar espacios extra en cada elemento.
       # - new_item y search_item no vacíos.
       # - Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

# TEST CASES: 
     # Normal:

# CODE
try:
    print("\nShopping list basics:\n")

    initial_items_text = input("Enter initial items: ").strip()

    if initial_items_text:  
        items_list = [item.strip() for item in initial_items_text.split(",")]
    else:
        items_list = []

        new_item = input("Enter item to add: ").strip()
        if new_item:
            items_list.append(new_item)
            search_item = input("Enter item to search: ").strip()

            is_in_list = search_item in items_list

            print(f"Items list: {items_list}")
            print(f"Total items: {len(items_list)}")
            print(f"Found item: {is_in_list}")

except ValueError:
    print ("Error: Invalid Input")
except KeyboardInterrupt:
    print ("Error: Invalid Input")

"""
# PROBLEM 2: Points and distance with tuples
try:

    x1 = float(input("Please Insert x1"))
    y1 = float(input("Please Insert y1"))
    x2 = float(input("Please Insert x2"))
    y2 = float(input("Please Insert y2"))

    point_a = (x1, y1) 
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    mid_point = ((x1 + x2)/2, (y1 + y2)/2)

    print (f"Point A: {point_a}")
    print (f"Point B: {point_b}")
    print (f"Distance: {distance}")
    print (f"Midpoint: {mid_point}")

except ValueError:
    print ("Error: Invalid Input")
except KeyboardInterrupt: 
    print ("Error: Invalid Input 2")

# PROBLEM 3: Product catalog with dictionary
try:
    product_prices = {
        "apple": 10.0,
        "banana": 15.0,
        "orange": 12.0,
    }
    product_name = input("Please, Insert the name of product: ").lower().strip()
    if product_name in product_prices: 
        unit_price = product_prices[product_name]
        quantity = int(input("Please Insert the quantity: "))

        if quantity <= 0: 
            print ("Please, insert a number")
        else: 
            total_price = unit_price * quantity
            print (f"Unit Price: {unit_price}")
            print (f"Quantity: {quantity}")
            print(f"Total: {total_price}")
    else: 
        print ("Error: Product not found")

except ValueError:
    print ("Error: Invalid Input")
except KeyboardInterrupt:
    print ("Error: Invalid Input 2")

# PROBLEM 4: Student grades with dict and list

students_grades = {
    "Jorge": [70.0, 65.0, 90.0],
    "Ricardo": [80.0, 90.0, 10.0],
    "Isaac": [70.0, 80.0, 65.0],
    "Pepe": []
}
try:
    student_name = input("Please Insert the name of the student: ").strip().title()

    if len(student_name) == 0: 
        print ("Error: Invalid Input; Insert a Name")
    elif student_name not in students_grades: 
        print("This student are not in the University")
    else: 
        grade_list = students_grades[student_name]
        if len(grade_list) == 0:
            print("Error: no grades available for this student")
        else:
            average = sum(grade_list) / len(grade_list)
            passed = average >= 70.0
            print (f"Grades: {grade_list}")
            print (f"Average: {average:.2f}")
            print (f"Passed: {passed}")
except ValueError: 
    print ("Error: Invalidr Input")
except KeyboardInterrupt:
    print ("Error: Invalid Input 2")

# PROBLEM 5: Word frequency counter (list + dict)
try:
    sentence = input("Please insert the sentence: ").strip()

    if len(sentence) == 0:
        print ("Error: Try again, Insert a sentence")
    else: 
        sentence = sentence.replace(",","").replace(".","")
        sentence = sentence.lower()
        word_list = sentence.split()
        if len(word_list) == 0:
            print ("Error: Invalid Sentence")
        else: 
            freq_dict = {}
            for word in word_list:
                if word in freq_dict:
                    freq_dict[word] +=1
                else:
                    freq_dict[word] = 1
            most_common_word = max(freq_dict, key=freq_dict.get)

            print(f"Word List: {word_list}")
            print(f"Frequencies: {freq_dict}")
            print(f"Most common word: {most_common_word}")
except ValueError:
    print ("Error: Invalid Input")
except KeyboardInterrupt:
    print ("Error: Invalid Input 2")

# PROBLEM 6: Simple contact book (disctionary CRUD)
try:
    contac_book = {
        "Alice": 8341168943,
        "Julio": 8371193949,
        "Estimpi": 893393928,
    }
    action_text = input("Choose your action:" \
    "'ADD', 'SEARCH', 'DELETE': ").sprit().upper()

    if action_text not in ["ADD", "SEARCH","DELETE"]:
        print ("Error: Insert someone action")
    elif action_text == "ADD":
        name = input("Enter contact: ").strip()
        if len(name) == 0:
            print ("Error. Invalid name")
        else: 
            phone = input("Enter phone number: ").strip()
            if len(phone) == 0.:
                print ("Error: Invalid phone number")
            else: 
                contac_book[name] = phone
                print (f"Contact saved: {name,phone}")
    elif action_text == "SEARCH":
        name = input("Enter contact name: ").strip()
        if len(name) == 0:
            print ("Error: Invalid name")
        else: 
            if name in contac_book:
                print (f"Phone: {contac_book[name]}")
            else:
                print ("Error: contact not found")
    elif action_text == "DELETE":
        name = input("Enter contact name: ").strio()
        if len(name) == 0: 
            print ("Error: Invalid name")
        else: 
            if name in contac_book:
                del contac_book[name]
                print (f"Contact deleted: {name}")
            else: 
                print ("Error: Contact not found")
except KeyboardInterrupt:
    print("Error: Invalid Input")
"""