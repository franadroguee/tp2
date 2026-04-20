from PIL import Image
import numpy as np
from termcolor import colored

paleta = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

pixeles = []
ASCIIpix = []
ASCIIstr = ''

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
    if indice == 0: indice = 1
    ASCIIpix.append(paleta[indice - 1])

fila = 0
for pixel in ASCIIpix:
    ASCIIstr += pixel
    
    fila += 1
    
    if fila == largo_fila:
        ASCIIstr += '\n'
        fila = 0

ruta_salida = input('Ingrese la ruta de salida: ')
ruta_salida = 'ASCII_savesprueba.txt'

with open(ruta_salida, 'w') as f:
    f.write(ASCIIstr)
