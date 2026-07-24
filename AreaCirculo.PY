# esto recibe los valores de las variables  
A = float(input("ingrese el valor de A: "))
B = float(input("ingrese el valor de B: "))
C = float(input("ingrese el valor de c: "))


#calcula el area del circulo 
radio = A/2
pi = 3.14

area_circulo =  pi * radio**2

#calcular el area del rombo

Area_rombo = ((A + C) * B) / 2


Area_total = area_circulo - Area_rombo

print(f"el valor del area amarilla es igual a: {Area_total} ")