
# EXAMEN 2 Julio César Maldonado Acuña 

# PROBLEM 2: Rectangle area and perimter 

try:
    width = float(input("Ingresa el ancho del rectangulo: "))
    height = float(input("Ingresa la altura del rectangulo: "))
    
    if width <= 0 or height <= 0:
        print ("Ingresa numeros validos")
    else: 
        area_value = width * height
        perimeter_value = 2*width + 2*height

        print (f"Area: {area_value}")
        print(f"Perimeter: {perimeter_value}")
except: 
    print ("Error: Invalid Input")

# Pregunta de Rescate
# Fibonacci 
print ("\nFibonacci:")
try: 
    n_terms = int(input("\nIntroduce un número: "))
     
    fibonacci = [] 

    a = 0 
    b = 1
    for i in range(n_terms):
        fibonacci.append(a)
        a, b =b, a + b
    print (f"Número Ingresado: {n_terms}")
    print (f"Serie de Fibonacci: {fibonacci}")
except:
    print ("Introduce un Numero entero.")
