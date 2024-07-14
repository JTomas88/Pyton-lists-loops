# Ejemplo while: x empieza en 1. MIentras x sea menor que 6-->imprimirá x y le irá sumando 1
# x = 1
# while x < 6:
#   print(x)
#   x += 1

x = 20
while x >= 0:
    if(x == 0):
        print("LIFTOFF")
    elif (x % 5 == 0):
        print(f"{x}!")
    else:
        print(x)
    x -= 1