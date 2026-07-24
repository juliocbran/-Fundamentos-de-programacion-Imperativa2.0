# crear vainilla 2 dolares chocolate 3 dolares, 
# menu debe llamarse a si mismo si el usuario quiere pedir otro helado o 
# si mete un dato incorrecto
# se puede usar if, elif, else
def menu():
    print("________LA HELADERIA DON JULIO________\n")
    print("NUESTRO MENU:\n")
    print("1. Vainilla ($2 dolares)")
    print("2. Chocolate ($3 dolares)")
    print("0. Finalizar compra")
    print("______________________________________\n")

def pedidos(ventaTotal=0):
    # Definimos los costos
    vainilla = 2
    chocolate = 3
    
    menu()
    
    # Manejo de errores de entrada
    try:
        opcion = int(input("Ingrese la opcion que desea: "))
    except ValueError:
        print(" Error: Por favor, ingrese solo números.")
        return pedidos(ventaTotal) # vuelve a pedir si ingresa texto
    
    # 2. Caso Base: Si elige 0 se termina la recursividad y muestra el total
    if opcion == 0:
        print("\n=============================")
        print(f" ¡Gracias por tu compra!\n Total a pagar: ${ventaTotal} dolares")
        print("=============================")
        return ventaTotal

    # 3. Opción 1: Suma Vainilla y se llama a sí misma con el nuevo total
    elif opcion == 1:
        nuevoTotal = ventaTotal + vainilla
        print(f"-> Añadido Vainilla. Subtotal: ${nuevoTotal} dolares")
        return pedidos(nuevoTotal)

    # 4. Opción 2: Suma Chocolate y se llama a sí misma con el nuevo total
    elif opcion == 2:
        nuevoTotal = ventaTotal + chocolate
        print(f"-> Añadido Chocolate. Subtotal: ${nuevoTotal} dolares")
        return pedidos(nuevoTotal)

    # 5. Opción Inválida: Se llama a sí misma conservando el total actual
    else:
        print("-> Opción no válida.\n Intente de nuevo.")
        return pedidos(ventaTotal)

# Ejecutamos la función por primera vez
pedidos()