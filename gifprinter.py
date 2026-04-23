import numpy as np
from PIL import Image, ImageSequence
import os, time
import cv2

def video():
    # 2. Open the video file
    filepath = input('Ingrese el video: ')
    if '\'' in filepath or '\"' in filepath:
        filepath = filepath [1:-1]
    vidcap = cv2.VideoCapture(filepath)
    success, image = vidcap.read()
    count = 0
    images_saved = 0

    while success:
        # 3. Convert OpenCV BGR to RGB for Pillow
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 4. Convert NumPy array to Pillow Image object
        pil_image = Image.fromarray(image_rgb)
        
        # 5. Save the image
        if count % 3 == 0:
            frame_name = os.path.join('gifolder', f"{images_saved}.png")
            pil_image.save(frame_name)
            images_saved +=1
        
        # 6. Read next frame
        success, image = vidcap.read()
        count += 1
    
    vidcap.release()
    return images_saved -1

def gif():
    # Open the GIF
    filepath = input('Ingrese el gif: ')
    
    if '\'' in filepath or '\"' in filepath:
        filepath = filepath [1:-1]
        
    img = Image.open(input(filepath))

    # Iterate through each frame
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        # Save each frame
        frame.save(f"gifolder/{i}.png", "PNG")
        frames = i
    
    return frames

while True:
    mode = input('Seleccione un modo (gif/ vid): ')
    if mode == 'gif':
        frames = gif()
        break
    elif mode == 'vid':
        frames = video()
        break

for imagen in range(frames + 1):
    paleta = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

    foto = Image.open(f'gifolder/{imagen}.png').convert('L')
    pixeles = []
    ASCIIpix = []
    ASCIIstr = ''

    w, h = foto.size
    
    altura = 200
    ancho = int(w * altura / h)

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

    os.system('cls')
    for fila in ASCIIstr.split('\n'):
        print(fila)
    os.remove(f'gifolder/{imagen}.png')

os.system('cls')