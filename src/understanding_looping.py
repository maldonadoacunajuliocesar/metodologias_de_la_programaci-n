
    # Ciclo for 
magicians = ["ron", "harry", "hermione", "sanpe"]
print (magicians[0], magicians[1], magicians[2], magicians[3])

for magician in magicians:
    print(magician)
    print(magician.title())
    print (f"{magician.title()} ese fue un gran truco!")
    print("\n")

print ("Gracias a todos por participar en el show de magia!")

"""
    Identación:

    Python utiliza la identación para determnar cuando 
    una línea de código está conectada 
    a la línea de código anterior. 

    Básicamente, se utilizan 4 espacios en blanco para 
    obligarnos a escribir código ordenado y estructurado.

"""
# No olvidemos identar (donde se necesita)
# Ejemplo 

magicians = ["alice", "David", "Jorge"]
for magician in magicians: 
# print (magician) # Error
    print(magician) # Solución

# Identation Error 
# Logical Error 
magicians= ["Alice", "David", "Jorge", "Candelario"]
for magician in magicians: 
    print (magician)
print (f"Great{magician}!, I can't wait to see your next trick")

# Correct 
agicians= ["Alice", "David", "Jorge", "Candelario"]
for magician in magicians: 
    print (magician)
    print (f"Great{magician}!, I can't wait to see your next trick")

# Identación innecesaria 
message = "Hola Julio"
 #print(message)

# Logical Error 

agicians= ["Alice", "David", "Jorge", "Candelario"]
for magician in magicians: 
    print (magician)
    print (f"Great{magician}!, I can't wait to see your next trick")
    print (" Than you everyone")
print (" Than you everyone")

# Error de syntasis 
    # for magician in magicians (FALTA ":")  

