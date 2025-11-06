
# Listas 
# Una lista es una colección ordenada y mutable de elementos.
# Se definen utilizando corchetes [] y separando los elementos con comas.

fruits= ["Manzanas", "Banana", "Cereza"]
print(fruits) # Salida

# Lista - Strings
print ("Lista de Frutes:")
print(fruits[0]) # Acceder al primer elemento "Manzana"
print(fruits[1]) # Acceder al segundo elemento "Banana"
print(fruits[2]) # Acceder al tercer elemento "Cereza"

# Lista - Strings - Metodos 
print("Lista de Frutes con Métodos:")
print (fruits[0].upper()) 
print (fruits[1].title())

# Identifica el último elemento de una lista
print("Acceder al último elemento de la lista:")
print(fruits[-1]) # Acceder al último elemento "Cereza"
print(fruits[-2]) # Acceder al penúltimo elemento "Banana"
print(fruits[-3]) # Acceder al antepenúltimo elemento "Manzana"


# PREGUNTA DE EXAMEN ¿PORQUE UNA LISTA ES MUTABLE? Porque podemos cambiar sus elementos después de haberla creado.

message = f"Mi fruta favorita es {fruits[0].title()}."
print(message)

"""
     Agregar elemetos a una lista
     - append(): Agrega un elemento al final de la lista.
     El metodo append(elemento) con un solo argumento, que es el elemento que se desea agregar a la lista.

     - insert(): Inserta un elemento en una posición específica de la lista.
     El metodo insert (intex, element) toma dos argumentos:
          el índice donde se desea insertar el elemento y el elemento en sí.
"""
# append()
print ("\nAgregar elementos a una lista: Metodo append() \n")
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles) 
motorcycles.append("Ducati")
print(motorcycles)  

# insert() 
print ("\nAgregar elementos a una lista: Metodo insert() \n")
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)
motorcycles.insert(0, "Ducati")
print(motorcycles)
print (motorcycles[0])

# Eliminar elementos de una lista

"""
     - del: Elimina un elemento en una posición específica de la lista.
     La declaración del index elimina el elemento en la posición especificada sin devolverlo.
"""
print ("\nEliminar elementos de una lista: Metodo 'del' \n")
motorcycles = ["Honda", "Yamaha", "Suzuki"]  
print(motorcycles)
del motorcycles[0]            
print(motorcycles)

# Eliminaer elemento de una lista igual a una variable
"""
     - pop(): Elimina y devuelve el último elemento de la lista.
     El método pop() elimina el último elemento de la lista y lo devuelve para que pueda ser utilizado posteriormente.
"""
print ("\nEliminar elementos de una lista: Metodo 'pop()' \n")
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print (f'La motocicleta que fue eliminada es: {popped_motorcycle.title()}')

# Eliminar elementos de una lista popo (index)

"""
     -pop (indez): Elimina y devuelve un elemento en una posición específica de la lista.
     El método pop(index) elimina el elemento en la posición especificada y lo devuelve.
 
"""
print("\nEliminar elementos de una lista: Metodo 'pop(index)' \n")
motorcycles = ["Honda", "Yamaha", "Suzuki"]  
print(motorcycles)
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta que tuve fue una {first_owned.title()}.')

# Eliminar elemento de una lista por valor
"""
     - remove(): Elimina la primera aparición de un valor específico en la lista.
     El método remove(value) busca la primera aparición del valor especificado en la lista y lo elimina.
"""
print("\nEliminar elementos de una lista: Metodo 'remove()' \n")
motorcycles = ["Honda", "Yamaha", "Suzuki", "Ducati"]
print(motorcycles)
motorcycles.remove("Ducati")
print(motorcycles)


# Actividad 
name = ['ana', 'juan','pedro','maria']
print(name)
deleted_name = input("\n \n Ingrese el nombre que desea eliminar de la lista: ")
name.remove(deleted_name.strip().lower())
print(name)
