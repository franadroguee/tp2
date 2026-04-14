from PIL import Image
import numpy as np
from termcolor import colored

p_rojo = []
p_azul = []
p_verde = []

foto = Image.open(str(input('Ingrese una imagen: ')))
w, h = foto.size
new_h = int(h * 306 / w)
img = foto.resize((306, new_h))

matriz = np.array(img)

for fila in matriz:
    largo_fila = len(fila)
    for pixel in fila:
        p_rojo.append(pixel[0])
        p_verde.append(pixel[1])
        p_azul.append(pixel[2])
        
fila = 0
for pixel in range(len(p_rojo)):
    print(colored('▓▓', (p_rojo[pixel], p_verde[pixel], p_azul[pixel])), end = '')
    
    fila += 1
    
    if fila == largo_fila:
        print('')
        fila = 0
    