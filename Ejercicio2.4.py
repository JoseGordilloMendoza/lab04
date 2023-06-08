from interpreter import draw
from chessPictures import *

# un cuadrado con su negativo a su derecha
base = cuadrado.join(cuadrado.negative())

# Crear una figura compuesta por la repetición horizontal de la base 4 veces
figure = base.horizontalRepeat(4)

# Dibujar la figura
draw(figure)