def sumaNaturales (numeros):
    
    if numeros == 0:
        return 0
    else:
        return numeros + sumaNaturales (numeros -1)
    
print (sumaNaturales(4))