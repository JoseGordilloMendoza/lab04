from interpreter import draw
from chessPictures import *

# La primera línea tendra al caballo y su negativo a la derecha
line1 = elCaballo.join(elCaballo.negative())

# La linea 2 refleja horizontalmente a la linea1
line2 = line1.horizontalMirror()

# Unimos la linea 1 con la linea 2
figure = line1.up(line2)

# Dibujamos
draw(figure)