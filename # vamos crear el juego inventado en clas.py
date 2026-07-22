# vamos crear el juego inventado en clase
import sys 
import time

def animacionPar():
    #doble barra \ para que Python imprima una sola \
    frames = [
        "🏃‍♂️ o         🏃‍♂️",
        "🏃‍♂️   o       🏃‍♂️",
        "🏃‍♂️     o     🏃‍♂️",
        "🏃‍♂️       o   🏃‍♂️",
        "🏃‍♂️         o 🏃‍♂️"
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
        "🏃‍♂️          o🏃‍♂️",
        "🏃‍♂️        o  🏃‍♂️",
        "🏃‍♂️      o    🏃‍♂️",
        "🏃‍♂️    o      🏃‍♂️",
        "🏃‍♂️  o        🏃‍♂️"
    ]
    for frame in frames:
        # \r sobrescribe la línea actual en la consola
        sys.stdout.write('\r' + frame)
        sys.stdout.flush() # Fuerza a la consola a dibujar inmediatamente
        time.sleep(0.2)    # Pausa de 0.2 segundos por fotograma

    print() # Un salto de línea al final para que el siguiente texto no se pegue




def juegoDeOperaciones():
    
    posJugador = 0
    valor = 0
    puntaje = 12

    while valor <= puntaje:
        if posJugador % 2 == 0:
            
          #  print(f"jugador {posJugador}, {animacionPar()}, {valor} ")

            valor = valor + 2
            
            print(f"jugador {posJugador}, {animacionPar()}, puntajes {valor} ")


        elif posJugador % 2 == 1:
            valor = valor - 1

            #animacionImpar()

           

        posJugador = posJugador + 1

juegoDeOperaciones()