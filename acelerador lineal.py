
#lista de flujo de compuertas
compuertas = ['A', 'P', 'R', 'P', 'A']

#solicitud de datos de usuario 
#eInicial = float(input("ingrese el valor en Joules de energia inicial:"))
#eFreno = float(input("ingrese el valor en Joules de la energia de freno:"))
#eImpulso = float(input("ingrese el valor en Joules de la energia de impulso:"))


eInicial = 20
eFreno = 5
eImpulso = 10

limite = 15
#definiciones de control

particulaViva = True
motivoDeParada = ""
compuertaActual = 0

#bucle mientras tanto... 

while compuertaActual < len(compuertas) and particulaViva:
    #creo una nueva variable para almacenar la compuerta actual que inicio con 0 
    compuerta = compuertas[compuertaActual]
    
    #creo la compuerta tipo A o compuerta de aceleracion
    if compuerta == 'A':
        
    #evaluo si la partucula tiene eneriga para pasar y si es asi le doy el impulso   
        if eInicial >= limite:
            print(f"Inicio: La energia inicial es {eInicial} joules")
            eInicial += eImpulso
            print(f"Compuerta A: La particula ha sido impulsada {eImpulso} joules, su nuevo valor es: {eInicial} joules")
    #evaluo cuando la energia es menos a 15 y le aplico el aumento para ver si alcaza el minimo para pasar
        elif eInicial < limite:
            print("Compuerta A: Perdida de eficiencia, se le aplicara la mitad del la energia de impulso")
            eInicial = eInicial + (eImpulso * 0.5 )
            if eInicial >= limite:
                print(f"Compuerta A: La particula ha sido impulsada {eImpulso * 0.5} joules, su nuevo valor es: {eInicial} joules")
   #criterio de parada por descarga total del sistema 
            elif eInicial < 0:
                print(f"Compuerta A: la energia de la particula no alcanzo el minimo requerido")
                particulaViva = False
                motivoDeParada = "descarga total del sistema."
                print(motivoDeParada)
                break
            
    #creo la compuerta de freno tipo P  
    elif compuerta == 'P':
    #Evaluo si la energia es mayor a 0     
        if eInicial > 0:
            eInicial -= eFreno
        print(f"Compuerta P: Energía disminuida a: {eInicial} Joules")
        
     #criterio de parada por descarga total del sistema
        if eInicial < 0:
            print(f"Compuerta P: la energia de la particula no alcanzo el minimo requerido")
            particulaViva = False
            motivoDeParada = "descarga total del sistema."
            print(motivoDeParada)
            break
    #criterio de parada por zona de resonancia destructiva    
        if eInicial >= 1 and eInicial <= 5:
            particulaViva = False
            motivoDeParada = "zona de resonancia destructiva que le impide avanzar a la siguiente seccion."
            print(motivoDeParada)
            break
 
      
    #creo la compuerta resonante tipo R   
    elif compuerta == 'R':
        
        if int(eInicial) % 2 == 0:
            print(f"Compuerta R: La parte entera de {eInicial} es par")
            eInicial *= 1.2
            print(f"Compuerta R: Se le aplico a la particula un incremento del 20% de su energia, su nuevo valor es: {eInicial}joules")
            
        elif int(eInicial) % 2 != 0:
            eInicial -= 5
            print(f"Compuerta R: La particula ha perdido 5 joules, su nuevo valor es: {eInicial} joules")
            
        elif eInicial <= 0:
            
            particulaViva = False
            motivoDeParada = "La partícula se detuvo por falta de energía."
            print(motivoDeParada)
            break
            
    compuertaActual += 1


    
