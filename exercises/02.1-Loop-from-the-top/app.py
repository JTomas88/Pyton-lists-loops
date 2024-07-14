my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Modify the loop below to print from end to start
numeroElementos = len(my_sample_list)
print ("numero elementos ",numeroElementos)

print("desde el comienzo hasta final:")
for elemento in range(len(my_sample_list)):
    print(my_sample_list[elemento])

# elemento: serán las vueltas que de el for
# in range: construye un rango que va desde 0 a len(my_sample_list) que vale 14 (totalElementos)
#
print('-----------------------------------------------')
final_lista = numeroElementos - 1
for elemento  in range(len(my_sample_list)):
    print(my_sample_list[final_lista])
    final_lista = final_lista -1


