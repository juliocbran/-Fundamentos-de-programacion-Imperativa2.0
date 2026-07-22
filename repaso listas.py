#ejemplos para crear, recorrer listas
#int
numeros = [5,10,15]
print (numeros)
numeros[0] = 7
print (numeros)
numeros[2] = 99
print(numeros)
numeros.append(50)
print(numeros)
#str ejemplos para crear y eleminar elementos de una lista
compras = ["pan"]
print (compras)
compras.append("queso")
print (compras)
compras.append("arroz")
print (compras)
compras.append("yuca")
print (compras)
compras.pop(1)
print(compras)
#ejemplo para recorrer listas
frutas = ["manzanas", "peras","uvas"]
for fruta in frutas:
    print (fruta)
    print(" ")   
for producto in compras:
    print(producto)
    
    
tablero = [["1","2","3"] #fila 0
           ["4","5","6"] #fiLa 1
           ["7","8","9"] #fila 2
           ]


