
"""
    Vamos a realizar un programa que sume 
    números hasta que el usuario escriba la palabra "salir"

    EL programa también debe decirme cuantos números
    ingreso el usuario, cual fue el mínimo y cual fue
    el máximo. 

"""

sum_of_numbers = 0.0 
counter = 0 
mini_num = None 
maxi_num = None 

while True: 
    print("Ingresa la palabra 'salir' para terminar el programa")
    user_input = input("Ingresa una cantidad en pesos mexicanos (MXN)")

    # Centinel
    if user_input == "salir":
        break

    try: 
        quantity = float(user_input)
    except ValueError: 
        print ("Cantidad no válida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        print("Programa terminado por el usuario")
        break
    counter += 1 
    sum_of_numbers += quantity

    if mini_num is None or quantity < mini_num: 
        mini_num = quantity 
    if maxi_num is None or quantity > maxi_num:
        maxi_num = quantity 

print("SUM", sum_of_numbers)
print("CONTADOR", counter)
print("MAXIMO", maxi_num)
print("MINIMO0", mini_num)
