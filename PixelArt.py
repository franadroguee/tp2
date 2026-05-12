from PIL import Image
import numpy as np
from termcolor import colored

#*******************************************************************************************************************************
#***************************************************DEFINICION DE VARIABLES*****************************************************

p_rojo = []
p_azul = []
p_verde = []

#*******************************************************************************************************************************
#***************************************************DEFINICION DE FUNCIONES*****************************************************

def distanciaR(lista_de_colores, pixel):
    '''analiza todos los colores posibles y retorna el que se asemeje para el rojo'''

    mejor_color = lista_de_colores[0]

    for color in lista_de_colores:
        if abs(color - int(pixel[0])) < abs(mejor_color - int(pixel[0])):
            mejor_color = color

    return mejor_color

def distanciaG(lista_de_colores, pixel):
    '''analiza todos los colores posibles y retorna el que se asemeje para el verde'''

    mejor_color = lista_de_colores[0]

    for color in lista_de_colores:
        if abs(color - int(pixel[1])) < abs(mejor_color - int(pixel[1])):
            mejor_color = color

    return mejor_color

def distanciaB(lista_de_colores, pixel):
    '''analiza todos los colores posibles y retorna el que se asemeje para el blue'''

    mejor_color = lista_de_colores[0]

    for color in lista_de_colores:
        if abs(color - int(pixel[2])) < abs(mejor_color - int(pixel[2])):
            mejor_color = color

    return mejor_color
    
#*******************************************************************************************************************************
#********************************************************CODIGO A CORRER********************************************************

def PixelART():

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
    for i in range(0, h, tam_bloque):

        lineas_bloque = [""] * tam_bloque

        for j in range(0, w, tam_bloque):

            bloque = matriz[i:i+tam_bloque, j:j+tam_bloque] # recorre desde i hasta (i+tam_bloque), y de j a (j+tam_bloque)

            pixel_nuevo = bloque.mean(axis=(0,1)) # devuelve el color del bloque generado  

            r = distanciaR(colores_disponibles, pixel_nuevo)
            g = distanciaG(colores_disponibles, pixel_nuevo)
            b = distanciaB(colores_disponibles, pixel_nuevo)

            p_rojo.append(r)
            p_verde.append(g)
            p_azul.append(b)

            # reorganiza en el tamaño original 
            for k in range(tam_bloque):
                lineas_bloque[k] += colored('▓▓', (r, g, b)) * tam_bloque

        for linea in lineas_bloque:
            print(linea)


