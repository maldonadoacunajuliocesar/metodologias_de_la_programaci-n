
"""
    Vamos a realizar un programa que 
    defina un PIN como contrasea . 

    Depués vamos a darle 3 intentos 
    al usuario para escribir el PIN.

    Si el usuario escribe correctamente 
    el PIN, el programa debe mostrar 
    un mensaje de Aceceso Permitido.

    Si el usuario se equivoca, el progrma
    dece decirle cuanto intentos le quedan
    y en caso de que no le queden intentos
    el mensaje deve decir Acceso Denegado, 
    excediste tus intentos.
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3 

attempts = 0 

while attempts < MAX_ATTEMPTS: 
    user_pin = input("Ingresa tu PIN: ")
    if user_pin == CORRECT_PIN:
        print ("Acceso Permitido")
        break
    else:
        attempts += 1
        reamining_attemps = MAX_ATTEMPTS  - attempts
        if reamining_attemps > 0:
            print (f"PIN INCORRECTO: te quedan {reamining_attemps} intentos")
        else: 
            print("Ya no tienes intentos")
print ("Final")