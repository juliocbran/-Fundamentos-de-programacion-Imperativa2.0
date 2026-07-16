
#pedimos multiples datos en un solo input 


n,m = map(int,input("Ingrese las medidas N x M de La Plaza (separado por espacio):").split())
a = int(input("Ingrese el largo o ancho de la losas:"))


#calculamos alto y ancho total
ancho, alto = (n+a - 1) // a, (m+a-1)//a
print(ancho * alto)

#prueba de consumo de memoria
print(id(ancho), id(alto))



