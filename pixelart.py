from PIL import Image
import numpy as np
from termcolor import colored

p_rojo = []
p_azul = []
p_verde = []


foto = Image.open(str(input('Ingrese una imagen: ')))
tam_bloque = int(input('Ingrese el tamaño del bloque del pixelart: '))
w, h = foto.size
img = foto.resize((w//tam_bloque, h//tam_bloque))

colores_disponibles = []
salto_colores = int(input('Ingrese el salto de colores: '))
rango = (255 // salto_colores)

# colores
for color in range(0, 255, rango):
    colores_disponibles.append(color)
while len(colores_disponibles) >= salto_colores:
    colores_disponibles.pop()
colores_disponibles.append(255)
    
matriz = np.array(img)

for fila in matriz:
    largo_fila = len(fila)
    for pixel in fila:
        
        p_rojo.append(min(colores_disponibles, key=lambda x: abs(x - int(pixel[0]))))
        p_verde.append(min(colores_disponibles, key=lambda x: abs(x - int(pixel[1]))))
        p_azul.append(min(colores_disponibles, key=lambda x: abs(x - int(pixel[2]))))
        
fila = 0
for pixel in range(len(p_rojo)):
    print(colored('▓▓', (p_rojo[pixel], p_verde[pixel], p_azul[pixel])), end = '')

    fila += 1
    
    if fila == largo_fila:
        print('')
        fila = 0
    