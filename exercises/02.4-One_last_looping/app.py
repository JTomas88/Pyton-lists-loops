names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1] = 'Steven'

posicionesTotales = len(names) 
names[posicionesTotales-1] = 'Pepe'
names[0] = f"{names[2]} {names[4]}"

namesFor = len(names)-1
for vuelta in range(len(names)):
    print(names[namesFor])
    namesFor = namesFor-1

