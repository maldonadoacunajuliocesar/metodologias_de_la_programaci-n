# Fibonacci Series EN PYTHON 

    # Alumno: Julio César Maldonado Acuña 
    # Matrícula: 2530001 
    # Grupo: 1-2

# RESUMEN EJECUTIVO 
"""
    1.¿Qué es la serie de Fibonacci?
        La serie de Fibonacci es una secuencia de números en la
        que cada número es la suma de los dos anteriores. 
        Comienza con los números 0 y 1, y la sucesión continúa indefinidamente, 
        por ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, ...

    2.¿Qué significa “calcular la serie hasta un número de términos n”?
        Significa generar los primeros n términos de la serie de Fibonacci, 
        donde n es un número entero que el usuario proporciona.

    3. ¿Qué cubrirá tu programa?
        El programa leerá el valor de n (número de términos a generar), 
        realizará una validación básica para asegurarse de que n sea positivo,
        y luego calculará y mostrará los primeros n términos de la serie de
        Fibonacci.
"""
# PROBLEM: Fibonacci series up to n terms 

# Description:
       # Implementa un programa que calcule y muestre la serie de Fibonacci 
       # hasta n términos, donde n es ingresado por el usuario. La serie debe 
       # comenzar en 0 y 1, por lo que:

          # - Si n = 1 → salida: 0    
          # - Si n = 2 → salida: 0, 1  
          # - Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8

            # El programa debe:
                # 1) Leer n desde la entrada estándar.  
                # 2) Validar n.  
                # 3) Generar la serie de Fibonacci con un bucle (for o while).  
                # 4) Imprimir los términos en una sola línea, separados por espacios o comas.
   # Inputs: 
       # - n (int; número de términos de la serie a generar).
   # Outputs: 
       # "Number of terms:" <n> (opcional)
       # "Fibonacci series:" <term_1> <term_2> ... <term_n>
   # Validations:
       # - n debe poder convertirse a entero.
       # - n >= 1.
       # - (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
       # - Si la validación falla, NO calcular la serie.
# TEST CASES: 
     # Normal:
"""
Fibonacci:

Enter a number:: 5
Number Entered: 5
Fibonacci Sequence: [0, 1, 1, 2, 3]
"""
     # Border:
"""
Fibonacci:

Enter a number:: 1
Number Entered: 1
Fibonacci Sequence: [0]
"""
     # Error:
"""
Fibonacci:

Enter a number:: 60
Error: Enter numbers from 1 to 50.
"""

# CODE
print ("\nFibonacci:")
try: 
    n_terms = int(input("\nEnter a number: "))
    if n_terms >= 1 and n_terms <= 50:
        fibonacci = [] 
    
        a = 0 
        b = 1
        for i in range(n_terms):
            fibonacci.append(a)
            a, b =b, a + b
        print (f"Number Entered: {n_terms}")
        print (f"Fibonacci Sequence: {fibonacci}")
    else: 
        print("Error: Enter numbers from 1 to 50.")
except ValueError:
    print ("Enter an integer.")

# CONCLUSIONES 
"""
    El uso de un bucle fue clave para generar la serie de Fibonacci 
    de manera eficiente, ya que nos permitió calcular los términos de manera 
    iterativa sin necesidad de almacenar toda la secuencia previamente. 
    Esto simplificó el código y lo hizo más flexible. Además, es importante 
    manejar bien los casos especiales de n = 1 y n = 2, ya que estos casos 
    tienen una longitud mínima y no siguen el mismo patrón que los términos posteriores. 
    Finalmente, esta lógica de generar secuencias de números mediante un bucle es reutilizable
    en otros programas que requieran generar series matemáticas o secuencias numéricas 
    de manera similar, como la secuencia de tribonacci o secuencias aritméticas.
"""
# REFERENCIAS 

# 1) https://realpython.com/fibonacci-sequence-python/
# 2) https://www.geeksforgeeks.org/python/python-program-to-print-the-fibonacci-sequence/
# 3) https://www.delftstack.com/es/howto/python/fibonacci-sequence-python/


# REPOSITORIO DE GITHUB