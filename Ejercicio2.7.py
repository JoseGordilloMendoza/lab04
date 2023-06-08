from interpreter import draw
from chessPictures import *

# Establecemmos un cuadrado negro
negativeSquare = cuadrado.negative()

# Tengamos las fichas negras con su fondo de cuadrado alternado (claro y oscuro)
torreNegra1 = laTorre.negative().setBackground(cuadrado)
caballoNegro1 = elCaballo.negative().setBackground(negativeSquare)
alfilNegro1 = elAlfil.negative().setBackground(cuadrado)
reynaNegra = laReina.negative().setBackground(negativeSquare)
reyNegro = elRey.negative().setBackground(cuadrado)
alfilNegro2 = elAlfil.negative().setBackground(negativeSquare)
caballoNegro2 = elCaballo.negative().setBackground(cuadrado)
torreNegra2 = laTorre.negative().setBackground(negativeSquare)