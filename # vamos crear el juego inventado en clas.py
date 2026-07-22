# vamos crear el juego inventado en clase
import sys 
import time

def animacionPar():
    #doble barra \ para que Python imprima una sola \
    frames = [
        "✊🏐        ✊",
        "✊  🏐      ✊",
        "✊    🏐    ✊",
        "✊      🏐  ✊",
        "✊        🏐✊"
    ]
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.2)    # Pausa de 0.2 segundos por fotograma

    print() # Un salto de línea al final para que el siguiente texto no se pegue


def animacionImpar():
    #doble barra \ para que Python imprima una sola \
    frames = [
        "✊        🏐✊",
        "✊      🏐  ✊",
        "✊    🏐    ✊",
        "✊  🏐      ✊",
        "✊🏐        ✊"
    ]
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.2)    # Pausa de 0.2 segundos por fotograma

    print() # Un salto de línea al final para que el siguiente texto no se pegue




def juegoDeOperaciones():
    # Pedimos los datos al usuario antes de iniciar el bucle
    totalJugadores = int(input("Ingrese cantidad de jugadores: "))
    puntajeLimite = int(input("puntaje maximo: "))
    
    print("\n----- ¡Empieza el juego! -----\n")

    turno = 0
    valor = 0

    while valor <= puntajeLimite:
        # El operador % permite ciclar entre 1 y el total de jugadores
        num_jugador = (turno % totalJugadores) + 1

        # Evaluamos si el número del jugador es Par o Impar
        if num_jugador % 2 == 0:
            animacionPar()
            operacion = "+2"
            valor += 2
        else:
            animacionImpar()
            operacion = "-1"
            valor -= 1

        print(f"Turno {turno + 1} | Jugador {num_jugador} | Operación: {operacion} | Puntaje acumulado: {valor}\n")

        turno += 1

    print(f"🎉 ¡Juego terminado! Se alcanzó o superó el límite de {puntajeLimite} puntos.")

# Ejecutar el juego
juegoDeOperaciones()
