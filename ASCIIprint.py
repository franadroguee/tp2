from PIL import Image
import numpy as np
from termcolor import colored

paleta = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

pixeles = []
ASCIIpix = []

foto = Image.open(input('Ingrese una imagen: ')).convert('L')
w, h = foto.size

ancho = int(input('Ingrese el ancho de la imagen: '))
print('\n')
altura = int(h * ancho / w)
img = foto.resize((ancho, int(altura * 0.45)))

matriz = np.array(img)

for fila in matriz:
    largo_fila = len(fila)
    for pixel in fila:
        pixeles.append(255 - int(pixel))
        
for pixel in pixeles:
    indice = int(pixel * 70 / 255)
    ASCIIpix.append(str(paleta[indice - 1]))

fila = 0
for pixel in ASCIIpix:
    print(pixel, end = '')
    
    fila += 1
    
    if fila == largo_fila:
        print('')
        fila = 0
