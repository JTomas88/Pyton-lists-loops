# Remember to import random function here
import random


my_list = [4, 5, 734, 43, 45]
def generar_numeros():    
    for i in range(1, 11):
        numeroR = random.randint(1, 100)
        my_list.append(numeroR)
        i+=i
    return my_list

print(generar_numeros())



# The magic goes below



# def generate_random_list():
#     aux_list = []
#     randonlength = random.randint(1, 100)

#     for i in range(randonlength):
#         aux_list.append(randonlength)
#         i += i
#     return aux_list