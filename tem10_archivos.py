from io import open

texto = "Una linea con texto\n"

fichero = open("fichero.txt", "w")
fichero.write(texto*18)
fichero.close()

file = open("fichero.txt", "r")

print(file.read())
print(type(file))