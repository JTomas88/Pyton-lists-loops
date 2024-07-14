my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here

def sum_odds (lista):
    total = 0
    for elemento in lista:
        if (elemento % 2 !=0):
            total = total + elemento
    return total

print(sum_odds(my_list))