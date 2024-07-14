sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []

totalValores = len(sample_list)-1
for vuelta in range (len(sample_list)):
    new_list.append(sample_list[totalValores])
    totalValores = totalValores-1
print(new_list)
