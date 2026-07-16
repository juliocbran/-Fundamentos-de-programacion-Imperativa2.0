 


def esPrimo (parametro):
    if parametro <= 1 :    
        return False
    for i in range (2, parametro):
        if parametro % i == 0:
            return False 
    return True   
print(esPrimo(5))
print(esPrimo(4))
    
