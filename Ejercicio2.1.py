import pygame
pygame.init()

from interpreter import draw
from chessPictures import *

# Crear la primera línea como la unión del caballo y su negativo a la derecha
line1 = elCaballo.join(elCaballo.negative())

# Crear la segunda línea como la unión del negativo del caballo y el caballo original
line2 = elCaballo.negative().join(elCaballo)

# Combinar las dos líneas
figure = line1.up(line2)

# Dibujado
draw(figure)