
# CRUD en Python

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 
"""
    1. ¿Qué es un CRUD y qué significan Create, Read, Update, Delete?
        CRUD es un acrónimo que representa las operaciones básicas sobre datos: Crear (Create), Leer (Read),
        Actualizar (Update) y Eliminar (Delete). Estas operaciones son fundamentales en el manejo de cualquier base 
        de datos o estructura de almacenamiento de información.

    2. ¿Qué estructura de datos elegiste (dict o list de dicts) y por qué?
        Elegí utilizar un diccionario donde cada clave es un identificador único (`item_id`) y el valor es otro 
        diccionario que contiene los detalles del producto como `name`, `price`, y `quantity`. Esto permite un acceso 
        rápido y eficiente a cada producto utilizando su identificador único.

    3. ¿Cómo te ayuda usar funciones para organizar la lógica del CRUD?
        El uso de funciones permite dividir el programa en partes independientes, lo que facilita la comprensión, 
        reutilización y mantenimiento del código. Cada operación CRUD es encapsulada en su propia función, manteniendo 
        el código modular y fácil de extender.

    4. ¿Qué cubre tu programa?
        El programa cubre un menú principal que permite al usuario interactuar con el CRUD. Las operaciones de creación, 
        lectura, actualización y eliminación de elementos están implementadas como funciones separadas que interactúan 
        con una estructura de datos (diccionario o lista de diccionarios) para gestionar los productos.
"""
# PRINCIPIOS Y BUENAS PRÁCTICAS

"""
    1. Usar funciones para cada operación CRUD para mantener el código limpio y organizado.
    2. Validar las entradas para evitar datos incorrectos o mal formateados, como precios negativos o IDs duplicados.
    3. Utilizar estructuras de datos como diccionarios para un acceso rápido a los elementos mediante sus claves únicas.
    4. Mostrar mensajes claros al usuario indicando el éxito o error de las operaciones.
"""

# PROBLEM 1: In-memory CRUD manager with functions

    # Description:
        # Program that implements a simple CRUD system (Create, Read,
        # Update, Delete) for items stored in a dictionary and/or list.
        # Each CRUD operation is handled by its own function, and the user
        # interacts with the system through a text-based menu.
    # Inputs:
        # - Menu options selected by the user (string or int)
        # - For CREATE/UPDATE: item_id, name, price, quantity
        # - For READ/DELETE: item_id
    # Outputs:
        # - Messages indicating the result of each operation, such as:
        # - "Item created", "Item updated", "Item deleted",
        # - "Item not found", "Items list:", etc.
    # Validations:
        # - Menu option must be valid (for example, 0..4 or 0..5)
        # - item_id must not be an empty string
        # - Numeric fields (price, quantity) must be valid numbers >= 0
        # - Prevent creating items using an existing item_id
        # - For READ/UPDATE/DELETE: if item_id does not exist,
        #   display "Item not found"

# TEST CASE:
     # Normal:
"""
----- MENU -----
1) Create item
2) Read item by ID
3) Update item by ID
4) Delete item by ID
5) List all items
0) Exit
Choose an option: 1
Enter item ID: 001
Enter item name: Laptop
Enter item price: 1000
Enter item quantity: 5
Item created

----- MENU -----
1) Create item
2) Read item by ID
3) Update item by ID
4) Delete item by ID
5) List all items
0) Exit
Choose an option:
"""
     # Border:
"""

----- MENU -----
1) Create item
2) Read item by ID
3) Update item by ID
4) Delete item by ID
5) List all items
0) Exit
Choose an option: 1
Enter item ID: 002
Enter item name: Smartwatch
Enter item price: 200
Enter item quantity: 15
Error: item ID already exists

"""
     # Error:
"""
----- MENU -----
1) Create item
2) Read item by ID
3) Update item by ID
4) Delete item by ID
5) List all items
0) Exit
Choose an option: 1
Enter item ID:
Error: invalid input

"""

# CODE:

def create_item(items, item_id, name, price, quantity):
    """Creates a new item if item_id does not already exist."""
    if item_id in items:
        return False  # Duplicate ID not allowed
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    """Returns the item dictionary if found, otherwise None."""
    return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
    """Updates an existing item. Returns True if successful."""
    if item_id not in items:
        return False
    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items, item_id):
    """Deletes an item by id. Returns True if successful."""
    if item_id not in items:
        return False
    del items[item_id] 
    return True


def list_items(items):
    """Prints all items in a readable format."""
    if not items:
        print("No items available.")
        return
    print("Items list:")
    for item_id, data in items.items():
        print(f"- ID: {item_id}, Name: {data['name']}, Price: {data['price']}, Quantity: {data['quantity']}")

def main():
    items = {}  # Main data structure

    while True:
        print("\n----- MENU -----")
        print("1) Create item")
        print("2) Read item by ID")
        print("3) Update item by ID")
        print("4) Delete item by ID")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose an option: ").strip()

        # Validate menu option
        if option not in ["0", "1", "2", "3", "4", "5"]:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        # CREATE 
        if option == "1":
            item_id = input("Enter item ID: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            name = input("Enter item name: ").strip()
            if name == "":
                print("Error: invalid input")
                continue

            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: item ID already exists")

        # READ 
        elif option == "2":
            item_id = input("Enter item ID to read: ").strip()
            item = read_item(items, item_id)
            if item:
                print(f"Item found: Name = {item['name']}, Price = {item['price']}, Quantity = {item['quantity']}")
            else:
                print("Item not found")

        # UPDATE 
        elif option == "3":
            item_id = input("Enter item ID to update: ").strip()
            if item_id not in items:
                print("Item not found")
                continue

            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Error: invalid input")
                continue

            try:
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                if new_price < 0 or new_quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if update_item(items, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        # DELETE 
        elif option == "4":
            item_id = input("Enter item ID to delete: ").strip()
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == "5":
            list_items(items)


# Run the program
if __name__ == "__main__":
    main()
# CONCLUSIONES
"""
    El uso de funciones facilitó la organización del código y la implementación de cada operación CRUD de manera independiente. 
    Utilizar un diccionario como estructura de datos permitió un acceso eficiente y rápido a los elementos mediante sus identificadores 
    únicos. Los casos de validación fueron esenciales para garantizar la integridad de los datos y evitar errores, como IDs duplicados 
    o inexistentes. Este CRUD podría extenderse para manejar una base de datos o integrar características adicionales como búsqueda 
    avanzada y almacenamiento persistente.
"""
# REFERENCES
# 1) Python Official Documentation – Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Python Official Documentation – Functions
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 3) Real Python – Dictionaries in Python
#    https://realpython.com/python-dicts/
#
# 4) W3Schools – Python Functions Tutorial
#    https://www.w3schools.com/python/python_functions.asp
#
# 5) Programiz – Python Dictionary (Beginner Guide)
#    https://www.programiz.com/python-programming/dictionary

# Repositorio de GitHub