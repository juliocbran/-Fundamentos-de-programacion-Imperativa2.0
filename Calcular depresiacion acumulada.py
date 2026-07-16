#datos de entrada 
costoInicial = 20000 
VidaUtil = 6
valorRecuperacion = 2000
año = 2025

#calculo la depreciacion por año
depreciacion = ((costoInicial - valorRecuperacion) / VidaUtil)

depresiacionAcumulada = 0
# Encabezado de la tabla que voy a imprimir 
print("-" * 68)
print(f"|{'Año':<6}|{'Depreciación':<14}|{'Depreciación Acumulada':<24}|{'Valor del Automóvil':<12}|")
print("-" * 68)
print(f"| {año:<4} | {int(depreciacion):<12} | {int(depresiacionAcumulada):<22} | {int(costoInicial):<17} |")
#proceso 
vida = 0

depresiacionAcumulada += depreciacion

#Ciclo de repeticion para N (N = vidaUtil)
for vida in range(1, VidaUtil + 1):
 # Cálculos por cada ciclo
    añoSiguiente = año + vida
    depresiacionAcumulada = depreciacion * vida
    valorSiguiente = costoInicial - depresiacionAcumulada
    
#imprmimos el resultado de lo que acabamos de calcular
    print(f"| {añoSiguiente} | {int(depreciacion):<12} | {int(depresiacionAcumulada):<22} | {int(valorSiguiente):<17} |")