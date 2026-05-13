from PIL import Image
import numpy as np

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
  
def PixelART(ruta_foto):

    foto = Image.open(ruta_foto)
    tam_bloque = int(input('Ingrese el tamaño del bloque: '))

    p_rojo = []
    p_azul = []
    p_verde = []

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

    nueva_imagen = Image.new("RGB", (w, h))

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


            for y in range(i, min(i + tam_bloque, h)):
                for x in range(j, min(j + tam_bloque, w)):
                    nueva_imagen.putpixel((x, y), (r, g, b))

                nueva_imagen.save("PixelArt.png")

    print("Imagen guardada como PixelArt.png")
            

