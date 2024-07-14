# import the random package here "import random"
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list

my_stupid_list = generate_random_list()

# Write your code below this comment, good luck!
print(my_stupid_list)

the_last_one = my_stupid_list[-1]
print(the_last_one)



# aux_list -- lista vacia []
# randomlenght - genera un numero aleatorio - ejm 3

# for - va a dar desde 0 a 3 vueltas
#     aux_list.append --> agrega el 3 tantas vueltas como da el for 3. 
# retorna [3, 3, 3]
         
# my_stupid-list retorna [3, 3, 3,]