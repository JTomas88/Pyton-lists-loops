my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []

for elemento in my_list:
    if (isinstance(elemento, dict) or isinstance(elemento, list)):
        new_list.append(elemento)

print(new_list)

# lista = ['palabrastring', 2, [['lista2'], ['lista3']], 'palabraString2']

# # Crear una nueva lista vacía
# nuevaLista = []

# # Recorrer la lista original
# for elemento in lista:
#     # Comprobar si el elemento es de tipo str
#     if isinstance(elemento, str):
#         # Agregar el elemento a nuevaLista si es str
#         nuevaLista.append(elemento)

# # Imprimir la nueva lista
# print(nuevaLista)