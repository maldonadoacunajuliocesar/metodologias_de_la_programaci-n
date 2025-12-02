
"""
    Docstring for understanding_while_loop

    Utiilizamos el while loop para ejercutar un bloque
    de codigo mientras una condicion sea verdadera

    Estructura basica del while loop en Python:

        while condicion:
            # Bloque de codigo a ejecutar
"""
# Ejemplo basico de un while loop 
# Verificar si un núumero esta en un ranfo especifico (10 y entre 20)

while True: # While loop infinito
    try:
        number = int(input("Enter a number between 10 and 20:"))
 
        if number < 20 and number > 10:
            print("Numero dentro del rango")
            break
        else: 
            print("Numero fuera del rango")
    except ValueError: 
        print ("Entrada invalida, ingrese numero entero")
    except KeyboardInterrupt:
        print("Programa terminado por el usuario")
    break
