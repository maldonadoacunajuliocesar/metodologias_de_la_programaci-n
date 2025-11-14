
# Las tuplas son listas de elementos que no pueden cambiar su tamaño. Son inmutables
# Se utilizan los () para definir una tupla

# Rectángulo (largo, ancho)

rectangle_dimensions = (200,50) # Tupla 
print ("Largo:", rectangle_dimensions [0]) # 200 
print ("Ancho:", rectangle_dimensions [1]) # 50 

# Vamos a intentar modificar una tupla 
    # rectangle_dimensions [0] = 250 ERROR DE TIPO TYPERROR

for dimension in rectangle_dimensions: 
    print (dimension)

"""
     No podemos modificar una tupla, ni tampoco agregar/eliminar elementos.
     SI podemos hacer cambio de asignación a una variable que almancena una tupla.
"""
rectangle_dimensions = (300, 150) # Tupla 



