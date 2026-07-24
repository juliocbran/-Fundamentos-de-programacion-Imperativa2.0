def factorial (numero):
    # caso base
    if numero == 0:
        return 1
    
    else:
        #recursividad de n * fac de n -1
        return numero * factorial(numero - 1)
    
print(factorial(5))