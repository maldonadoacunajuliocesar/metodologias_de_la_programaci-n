
# SLICING 

players = ["cr7", "Messi", "Travis Kelce", "Chicarito", "Corona"]
print (players [0:3])

# Slice es trabajar con un grupo específico 
# de elementos de una lista 
print (players[1:4]) # = "Messi", "Travis Kelce", "Chicarito", 
print (players [:4]) # = "cr7", "Messi", "Travis Kelce", "Chicarito", "Corona"
print (players[2:])  # = "Messi", "Travis Kelce", "Chicarito", "Corona"

print (players [-3:]) # = "Travis Kelce", "Chicarito", "Corona"

# SLICING EN FOR 

players = ["cr7", "Messi", "Travis Kelce", "Chicarito", "Corona"]
first_three_players = players [0:3]
print ("First three players", first_three_players)

print ("Aqui vienen los tres mejores del salon: ")
for player in players [0:3]:
    print (player.upper())

# Copia de listas 
my_food =["Gorditas", "Pizza", "Machacado"]

# copy_of_food = my_food Manera errónea de copiar una lista 
copy_of_food_1 = my_food [:] 
copy_of_food_2 = my_food.coppy()
copy_of_food_3 = list(my_food)

# Modificando elementos 

cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars [0] = "bmw"
cars [1] = "porsche"
cars [2] = "mazda"
cars [3] = "toyota"

