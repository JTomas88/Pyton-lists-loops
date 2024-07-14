chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    listaConcatenada = []
    for elemento in list1:
        listaConcatenada.append(elemento)
    for element in list2:
        listaConcatenada.append(element)
    
    return listaConcatenada

    
print(merge_list(chunk_one, chunk_two))
