
"""
    Las listas también pueden almacenar números y de echo s
    son ideales para almancenarlos. 
    Python ofrece cantidad de funciones integradas para trabajar con listas de números.

    Por ejemplo, función range() genera una serie de números:
"""
# La función range() genera una serie de números
# en un rango especificado.
# Por ejemplo, para generar números del 0 al 9:
numbers = list(range(10))
print(numbers) # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] Imprime una lista 

print(type(numbers)) # Salida: <class 'list'>
print(type(numbers[0])) 

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num) # Imprime los números

for num in range (1,5):
    print (num)
numbers_1_to_4 = list(range (1,5))
print (numbers_1_to_4)

for num in range (1,10,2):  # Números impares 
    print (num)
odd_numbers = list(range(1,10,2))
print (odd_numbers) 

for num in range (2,10,2): # Números pares
    print (num)
even_numbers = list(range(2,10,2))
print (even_numbers)

#    Podemo crear cualquier tipo de listas de números con range() y list()
print ("\n Primero 10 números al cuadrdado: ")
squares = []
for value in range (1,11): 
    square = value ** 2 
    squares.append(square)
print (squares) 

# Métodos built - in para listas de números
print ("\n Métodos built - in para listas de números")4
digits = [1,2,3,4,5,6,7,8,9,0]
print ("Lista de digitos:", digits)
print ("Valor máximo:", max(digits)) # Valor máximo
print ("Valor mínimo:", min(digits)) # Valor mínimo
print ("Suma de todos los valores:", sum(digits)) # Suma de todos los valores
