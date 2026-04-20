from PIL import Image
import numpy as np
from termcolor import colored

paleta = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+','_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f','j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q','0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#','M', 'W', '&', '8', '%', 'B', '@', '$', '<', '>', '=', '!', '?', '^', '~','+', '-', '_', ':', ';', ',', '.', '@', '#', '$', '%', '&', '0', '1', '2','3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
        pixeles.append(int(pixel))
        
for pixel in pixeles:
    indice = int(pixel * 149 // 255)
    if indice == 0: indice = 1
    ASCIIpix.append(paleta[indice - 1])

fila = 0
for pixel in ASCIIpix:
    print(pixel, end = '')
    
    fila += 1
    
    if fila == largo_fila:
        print('')
        fila = 0
