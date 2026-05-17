from PIL import Image
import numpy as np
from termcolor import colored
import os


def ASCIIprint(ruta_foto):
    paleta = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

    pixeles = []
    ASCIIpix = []
    ASCIIstr = ''

    foto = Image.open(ruta_foto).convert('L')
    w, h = foto.size

    ancho = input('Ingrese el ancho de la imagen: ')
    
    while not ancho.isdigit():
        ancho = input('Ingrese el ancho de la imagen: ')
        
    ancho = int(ancho)
    
    altura = int(h * ancho / w)
    img = foto.resize((ancho, int(altura * 0.45)))

    matriz = np.array(img)

    for fila in matriz:
        largo_fila = len(fila)
        for pixel in fila:
            pixeles.append(255 - int(pixel))
            
    for pixel in pixeles:
        indice = int(pixel * 70 / 255)
        if indice == 0: indice = 1
        ASCIIpix.append(paleta[indice - 1])

    fila = 0
    for pixel in ASCIIpix:
        ASCIIstr += pixel
        
        fila += 1
        
        if fila == largo_fila:
            ASCIIstr += '\n'
            fila = 0

    nombre_archivo = input('Ingrese nombre que desea darle al archivo (solo nombre): ') # e.j.: Marylin

    with open(os.path.join('.', 'ASCII_saves', f'{nombre_archivo}.txt'), 'w') as file:
        file.write(ASCIIstr)
