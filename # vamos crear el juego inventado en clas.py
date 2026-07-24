# vamos crear el juego inventado en clase
import sys
import time


def animacion_par():
    frames = [
        "o         ",
        " o        ",
        "  o       ",
        "   o      ",
        "    o     ",
        "     o    ",
        "      o   ",
        "       o  ",
        "        o ",
        "         o"
    ]
    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    print()


def animacion_impar():
    frames = [
        "         o",
        "        o ",
        "       o  ",
        "      o   ",
        "     o    ",
        "    o     ",
        "   o      ",
        "  o       ",
        " o        ",
        "o         "
    ]
    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    print()


def juego_de_operaciones():
    while True:
        try:
            cantidad_jugadores = int(input("Ingrese la cantidad de jugadores: "))
            if cantidad_jugadores <= 0:
                print("La cantidad de jugadores debe ser un numero entero positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

    resultado = 0

    print(f"\nIniciando el juego con {cantidad_jugadores} jugadores...\n")

    for posicion in range(1, cantidad_jugadores + 1):
        if posicion % 2 == 1:
            resultado -= 1
            print(f"Jugador {posicion} (posicion impar): se resta 1 -> resultado = {resultado}")
            animacion_impar()
        else:
            resultado += 2
            print(f"Jugador {posicion} (posicion par): se suma 2 -> resultado = {resultado}")
            animacion_par()

    print(f"\nResultado final despues de {cantidad_jugadores} jugadores: {resultado}")

    if resultado <= cantidad_jugadores:
        print("El juego termina porque el resultado es menor o igual a la cantidad de jugadores.")
    else:
        print("El juego termino, pero el resultado es mayor que la cantidad de jugadores.")


if __name__ == "__main__":
    juego_de_operaciones()
