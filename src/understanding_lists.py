
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
     - insert(): Inserta un elemento en una posición específica de la lista.

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
