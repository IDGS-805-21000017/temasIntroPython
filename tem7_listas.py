import random as r

lista1 = [10, 5, 3]
lista2 = [1.5, 2.66 ,1.7, 89.2]
lista3 = ["Lunes", "Martes", "Miercoles"]
lista4 = ["Juan", 45, 1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

x = 0
suma = 0
while x < len(lista1):
    suma += lista1[x]
    x+=1

#{sum(lista1)}

print(f"La suma es {suma}")

lista5 = []
for i in range(0,10):
    lista5.append(r.randint(1,100))

#print(lista5)
#num = lista5.pop()
#print(f"Salio el numero {num} y es {type(num)}")
#print(f"Promedio {sum(lista5)/len(lista5)}")

def ejercicio():
    cantidad = int(input("Dame el rango de numeros"))
    pares, nones = [], []

    for i in range(0,cantidad):
        if i % 2 == 0:
            pares.append(i)
        else:
            [nones.append(i)]
    return (pares, nones)

if __name__ == "__main__":
    list1, list2 = ejercicio()
    print(f"Los pares son {list1}")
    print(f"Los nones son {list2}")