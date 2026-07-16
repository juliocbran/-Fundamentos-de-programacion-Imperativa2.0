palabra = str(input("ingrese la palabra:"))

def contarVocales (palabra):
    contador = 0
    vocales = "aeiouAEIOU"
    for letra in palabra:
        for vocal in vocales:
            if letra == vocal:
                    
                contador += 1

    return contador

print(contarVocales(palabra))
