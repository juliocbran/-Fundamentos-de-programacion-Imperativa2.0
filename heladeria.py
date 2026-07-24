# crear vainilla 2 dolares chocolate 3 dolares, 
# menu debe llamarse a si mismo si el usuario quiere pedir otro helado o 
# si mete un dato incorrecto
# se puede usar if, elif, else

def menu():

    
    print("_________BIENVENIDO A LA ELADERIA DON JULIO____________")
    print(" ")

    print("NUESTRO MENU:\n")
    # helado vainilla 
    print("1. HELADO DE VAINILLA: $2 DOLARES\n")
    # helado chocolate
    print("2. HELADO DE CHOCOLATE: $3 DOLARES\n")
    #SALIR
    print("3. TERMINAR COMPRA\n")

    print(" _______________________________________________________\n")



def pedidos():
    
    menu()
    try:
        opcion = int(input("ingrese la opcion que desea: "))
    except ValueError:

        opcion = pedidos()


pedidos()