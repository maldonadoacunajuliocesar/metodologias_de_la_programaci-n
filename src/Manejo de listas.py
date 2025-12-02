# MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 

# PROBLEM 1: Shopping list basics (list operations)
"""
try:
    initial_items_text = input("Ingresa la lista de productos: ")

    if len(initial_items_text) == 0:
        print ("Error: Invalid Input")
    else:
        items_lists = initial_items_text.split(",")
        items_lists = [item.strip() for item in items_lists if item.strip() != ""]
        print(items_lists)

except ValueError:
    print ("Error: Invalid Input")
except KeyboardInterrupt:
    print ("Error: Invalid Input")


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
"""
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