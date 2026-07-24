#repaso listas
fila = int(input("ingrese la cantidad de filas:"))
columna = int(input("ingrese la cantidad de columnas:"))

Matrix = []

for filas in range (fila):

    listaf = []

    for elementos in range (columna):
        listaf.append(int(input(f"introduce en elemento {elementos} de la lista {filas}:")))
    Matrix.append(listaf)

for listaf in Matrix:
    print(listaf)

