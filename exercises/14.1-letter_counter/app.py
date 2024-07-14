par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
parSinEspacios = par.replace(" ", "")
print(parSinEspacios)

parFinal = parSinEspacios.lower()
print(parFinal)

counts = {}

for letra in parFinal:
    if letra in counts:
        counts[letra] += 1
    else:
        counts[letra] = 1

print(counts)


