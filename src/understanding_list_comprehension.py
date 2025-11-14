
# List Comprehensions 

"""
    Una list comprehension combina el for loop 
    y la creación de nuevos elementos en una sola
    línea de código y también, automáticamente 
    agrea el nuevo elemento a la lista, es decir, 
    sin utilizar el append
"""

squares_list = [num **2 for num in range (10)]
print(squares_list)

# Números pares con el range
even_number_0_100 = list(range(0,101,2))

# Números pares utilizando list comprehension 
even_list_compre = [value for value in range (0,101)if value %2 == 0]
print (even_list_compre)


