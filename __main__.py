from PIL import Image

from PIL import Image

foto = Image.open('monalisa.jpg')
tam = 30

# Achicás y volvés a agrandar — PIL promedia los bloques automáticamente
pequeña = foto.resize(
    (foto.width // tam, foto.height // tam),
    Image.NEAREST
)
resultado = pequeña.resize(foto.size, Image.NEAREST)
resultado.save('resultado.jpg')