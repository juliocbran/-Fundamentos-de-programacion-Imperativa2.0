
#pedimos multiples datos en un solo input
n,m,a = map(int,input("Ingrese la Base de la losas:").split())

#calculamos alto y ancho total
ancho, alto = (n+a - 1) // a, (m+a-1)//a

print(id(ancho), id(alto))
print(ancho * alto)


