import pygame, sys
from pygame.locals import *
from colors import *

# Función para dibujar una línea en la ventana de visualización
def parseLine(DISPLAY, y, s):
  x = 0
  for c in s:
    pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
    x += 1