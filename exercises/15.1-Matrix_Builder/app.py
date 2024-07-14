# Your code here
def matrix_builder (numero):
    tablero = []    
    for i in range(numero):
        fila = []
        for z in range(numero):
            fila.append(1)    
        tablero.append(fila)
    
    return tablero


result = matrix_builder(3)
print (result)



