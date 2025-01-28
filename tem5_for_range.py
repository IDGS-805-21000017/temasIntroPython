from time import sleep as sl

numeros = [4,8,6,1,2]
numeros1 = list(range(1,100,5))
pares = []
nones = []

datos = [{"luis", 25}, {"alberto", 13},{"jorge", 18}]

for numero in numeros:
    print(numero)

for numero in numeros1:
    if numero/2 ==  0:
        pares.append(numero)
    else:
        nones.append(numeros)
print(pares)
print(nones)


for i in range(50):
    print(i)
    sl(0.5)