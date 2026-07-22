#punto 1

#Elaborar un algoritmo que permita determinar cuál es el ganador de la beca de entre dos
#estudiantes. El algoritmo deberá hallar la nota definitiva de cada uno de ellos (4 materias,
#ingrese sus notas y calcule el promedio) Si es mayor que 4.5 el alumno podrá aspirar a la
#beca, de lo contrario no.

#pedimos las notas y el nombre del estudiante numero 1
st1 = input("ingrese el nombre del estudiante 1:")
nt11 , nt12 , nt13 , nt14 = map(float, input(F"ingrese las 4 notas de {st1} separadas por espacios:").split())    

#pedimos las notas y el nombre del estudiante numero 2
st2 = input("ingrese el nombre del estudiante 2:")
nt21 , nt22 , nt23 , nt24 = map(float, input(f"ingrese las 4 notas de {st2} separadas por espacios: ").split())

#en base a las notas sacadas por el estudiante, sacamos el promedio de la nota final
promedio1 = (nt11 + nt12 + nt13 + nt14)/4
promedio2 = (nt21 + nt22 + nt23 + nt24)/4

#condicionales que evaluan si el estudiante paso o no la materia
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
