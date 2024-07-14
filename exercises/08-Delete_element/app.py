people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    nuevaLista = []
    people.remove(person_name)
    nuevaLista = people[:]
    return nuevaLista
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))



