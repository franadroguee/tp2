alumnos = [('Nombre1', 'Apellido1', 'Nota1'), ('Nombre2', 'Apellido2', 'Nota2')]
import random

lista_alumnos = {1: [], 2: [], 3: [], 4: []}

p4_1 = 0.5
p4_2 = 0.3
p4_3 = 0.2
grupos = []

notas = {'mb': 4, 'b': 3, 'r': 2, 'i': 1}

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
        if letra == ' ':
            n_resuelto += ' '
        else:
            n_letra = alfabeto.index(letra)
            
            if n_letra - desp_cesar < 0:
                n_letra += 26
                
            n_resuelto += alfabeto[n_letra - desp_cesar]

    return n_resuelto

for nombre, apellido, nota in alumnos:
    nombre = cifrado(nombre.upper())
    apellido = cifrado(apellido.upper())
    
    lista_alumnos[notas[nota]].append(f'{nombre} {apellido}')
    
while lista_alumnos[1] != [] or lista_alumnos[2] != [] or lista_alumnos[3] != [] or lista_alumnos[4] != []:
    for nota in lista_alumnos.keys():
        for alumno in lista_alumnos[nota]:
            lista_alumnos[nota].remove(alumno)
            prob = random.random()
            
            if prob <= p4_1:
                inicio = 1
            elif prob <= p4_2:
                inicio = 2
            else:
                inicio = 3      
            
            pareja = False
            for grupo in  range(inicio, 5):
                if lista_alumnos[grupo] != []:
                    eleccion = random.choice(lista_alumnos[grupo])
                    while eleccion == alumno:
                        eleccion = random.choice(lista_alumnos[grupo])
                    lista_alumnos[grupo].remove(eleccion)
                    pareja = True
                    break
                    
            if not pareja:
                int1, int2 = grupos[len(grupos) -1]
                grupos.pop()
                grupos.append((int1, int2, descifrado(alumno)))
                break
                    
            grupos.append((descifrado(alumno), descifrado(eleccion)))
            
busqueda = input('Ingrese el nombre y apellido del estudiante, separados por un espacio: ').upper()

resultado = False
for int1, int2, *int3 in grupos:
    if int3 != []:
        int3= int3[0]
    else:
        int3 = None
    if busqueda == int1 or busqueda == int2 or busqueda == int3:
        print(f'{int1}, {int2}' + f', {int3}' if int3 is not None else '')
        resultado = True
        
if not resultado:
    print('Lo sentimos, el alumno no fue encontrado')