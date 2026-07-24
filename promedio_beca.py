
st1 = input("ingrese el nombre del estudiante 1:")
nt11 , nt12 , nt13 , nt14 = map(float, input(F"ingrese las 4 notas de {st1} separadas por espacios:").split())
    

st2 = input("ingrese el nombre del estudiante 2:")
nt21 , nt22 , nt23 , nt24 = map(float, input(f"ingrese las 4 notas de {st2} separadas por espacios: ").split())

promedio1 = (nt11 + nt12 + nt13 + nt14)/4
promedio2 = (nt21 + nt22 + nt23 + nt24)/4

if promedio1 > promedio2:
    if promedio1 >= (4.5):
        print(f"{st1} tiene un promedio de {promedio1} y es el ganador de la beca")
    else:
        print(f"{st1} tiene un promedio de {promedio1} pero no fue suficiente para ganar la beca")
else:
    if promedio2 >= (4.5):
        print(f"{st2} tiene un promedio de {promedio2} y es el ganador de la beca")
    else:
        print(f"{st2} tiene un promedio de {promedio2} pero no es sificiente para ganar la beca")
        