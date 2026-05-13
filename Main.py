import ASCIIprint 
import PixelArt
import os 

foto = input('Ingrese la ruta de su imagen: ')

while not os.path.exists(foto):
    foto = input('Ingrese una ruta correcta: ')


Tipo_imagen = input(f'Ingrese el tipo de imagen que quiere imprimir (ASCII / Pixel-ART): ')

while Tipo_imagen != "ASCII" and Tipo_imagen != "Pixel-ART":
    Tipo_imagen = input(f'Ingrese un tipo de imagen valido: ')


if Tipo_imagen == "ASCII":
    ASCIIprint.ASCIIprint(foto)

elif Tipo_imagen == "Pixel-ART":
    PixelArt.PixelART(foto)

