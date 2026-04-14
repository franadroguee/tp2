from PIL import Image
import numpy as np
from termcolor import colored

paleta = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

pixeles = []
ASCIIpix = []

foto = Image.open(str(input('Ingrese una imagen: ')))
w, h = foto.size

ancho = int(input('Ingrese el ancho de la imagen: '))
altura = int(h * ancho / w)
img = foto.resize((ancho, int(altura * 0.45)))

colores_disponibles = []
rango = (255 // 70)

# colores
for color in range(0, 255, rango):
    colores_disponibles.append(color)
print(colores_disponibles)

matriz = np.array(img)

for fila in matriz:
    largo_fila = len(fila)
    for pixel in fila:
        pixeles.append((pixel[0] + pixel[1] + pixel[2]) // 3)
        
for pixel in pixeles:
    indice = min(colores_disponibles, key=lambda x: abs(x - pixel[0]))
    ASCIIpix.append(paleta[indice])

fila = 0
for pixel in ASCIIpix:
    print(pixel, end = '')
    
    fila += 1
    
    if fila == largo_fila:
        print('')
        fila = 0
