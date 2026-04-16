alumnos = [('ejemplo', 'mb'), ('ejemplo2', 'r')]

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cifrado(nombre):
    desp_cesar = 3
    n_encrip = ''
    for letra in nombre:
        n_letra = alfabeto.index(letra)
        
        if n_letra + desp_cesar >= len(alfabeto):
            n_letra -= 26
            
        n_encrip += alfabeto[n_letra + desp_cesar]
        
    return n_encrip
        
def descifrado(nombre):
    desp_cesar = 3
    n_resuelto = ''
    for letra in nombre:
        n_letra = alfabeto.index(letra)
        
        if n_letra - desp_cesar < 0:
            n_letra += 26
            
        n_resuelto += alfabeto[n_letra - desp_cesar]

    return n_resuelto

print(descifrado(cifrado('XYZ')))
    
