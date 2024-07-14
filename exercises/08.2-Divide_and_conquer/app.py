list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even (lista):
    sorted_list = [] #impares
    even = []        #pares
    unionSortedEven = []  #une las 2 listas anteriores
    for elemento in lista:
        if (elemento % 2 == 0):
            even.append(elemento)
        else: 
            sorted_list.append(elemento)
    
    for element in sorted_list:
        unionSortedEven.append(element)
    for element in even:
        unionSortedEven.append(element)
    
    return unionSortedEven

print(sort_odd_even(list_of_numbers))

