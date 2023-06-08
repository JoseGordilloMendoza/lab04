import pygame
pygame.init()

from interpreter import draw
from chessPictures import *

# Crear la base del tablero (un cuadro negro seguido de un cuadro blanco)
base = cuadrado.join(cuadrado.negative())
# Su negativo es lo contrario
negativeBase = base.negative()

# Una fila estara compuesta por 4 veces la base
row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

# Combinar las filas en pares, la fila original encima y la negativa abajo
rowPair = row.up(negativeRow)

# Figura compuesta por las filas repetidas verticalmente
figure = rowPair.verticalRepeat(2)

# Dibujar la figura
draw(figure)