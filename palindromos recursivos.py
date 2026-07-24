def palindromos (palabra):
    if len (palabra) <= 1:
        return "Es palindromos"
    
    else:
        if palabra[0] == palabra [-1]:
            return palindromos (palabra[1:-1])
        else: 
            return "No es palindromo"
    
    
print (palindromos ("reconocer"))  
     