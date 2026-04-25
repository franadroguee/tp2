from PIL import Image
import numpy as np
from termcolor import colored

#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------DEFINICION DE VARIABLES---------------------------------------------------

p_rojo = []
p_azul = []
p_verde = []

#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------DEFINICION DE FUNCIONES---------------------------------------------------

def distanciaR(x):
    '''analiza todos los colores posibles y retorna el que se asemeje para el rojo'''
    return abs(x - int(pixel[0]))

def distanciaG(x):
    '''analiza todos los colores posibles y retorna el que se asemeje para el verde'''

    return abs(x - int(pixel[1]))

def distanciaB(x):
    '''analiza todos los colores posibles y retorna el que se asemeje para el blue'''

    return abs(x - int(pixel[2]))
    
#-------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------CODIGO A CORRER-------------------------------------------------------

foto = Image.open(input('Ingrese una imagen: '))
tam_bloque = int(input('Ingrese el tamaño del bloque: '))

colores_disponibles = []
salto_colores = int(input('Ingrese el salto de colores: '))
rango = 255 // salto_colores

for color in range(0, 255, rango):
    colores_disponibles.append(color) # lista con los valores posibles

while len(colores_disponibles) >= salto_colores:
    colores_disponibles.pop()
colores_disponibles.append(255) # elimina el ultimo y lo remplazar por el 255

matriz = np.array(foto) # transforma a la imagen en una matriz 

h, w, _ = matriz.shape

# aplica los colorees nuevos agrupandolos en las dimensiones nuevas de los pixeles ingresadas (tam_bloque) 
for i in range(h):
    for j in range(w):

        pixel = matriz[i][j]

        r = min(colores_disponibles, key=distanciaR)
        g = min(colores_disponibles, key=distanciaG)
        b = min(colores_disponibles, key=distanciaB)

        p_rojo.append(r)
        p_verde.append(g)
        p_azul.append(b)

        print(colored('▓▓', (r, g, b)), end='')

    print()
