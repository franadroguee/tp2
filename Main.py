import ASCIIprint 
import PixelArt

Tipo_imagen = input(f'Ingrese el tipo de imagen que quiere imprimir (ASCII / Pixel-ART): ')

while Tipo_imagen != "ASCII" and Tipo_imagen != "Pixel-ART":
    Tipo_imagen = input(f'Ingrese un tipo de imagen valido: ')


if Tipo_imagen == "ASCII":
    ASCIIprint.ASCIIprint()

elif Tipo_imagen == "Pixel-ART":
    PixelArt.PixelART()

