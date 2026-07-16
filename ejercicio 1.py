#este codigo calcula la altura de un edificio usando como punto de referencia un arbol 
#de este se toma su altura y la distancia desde el arbol hata la sombra que se crusa con el edificio
#tambien se toma la distancia desde el edificio hatsa la sombra donde llega o se cruza con el arbol 


alturaB = int(input("ingrese el valor de la altura menor: "))
baseA = int(input("ingrese el valor de la base mayor: "))
baseB = int(input("ingrese el valor de la base menor: "))

alturaA = int(((baseA/baseB) * alturaB))

print(f"la altura del edificio es {alturaA} MT")