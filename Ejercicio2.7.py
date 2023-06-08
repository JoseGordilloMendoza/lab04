from interpreter import draw
from chessPictures import *

# Establecemos un cuadrado negro
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

# Fila de piezas negras, siguiendo la base anterior
row1 = torreNegra1.join(caballoNegro1).join(alfilNegro1).join(reynaNegra).join(reyNegro).join(alfilNegro2).join(caballoNegro2).join(torreNegra1)

# Par de peones negros, en este caso, estos deben empezar con el fondo oscuro
coupleBlackPawn = elPeon.negative().setBackground(negativeSquare).join(elPeon.negative().setBackground(cuadrado))

# Creamos una fila de peones negros, siendo la segunda fila (luego de la anterior)
row2 = coupleBlackPawn.horizontalRepeat(4)

# Base del tablero
base = cuadrado.join(cuadrado.negative())
negativeBase = base.negative()

# Una fila de tablero vacia con su negativo
row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

# Par de lineas vacias alternadas
rowPair = row.up(negativeRow)

# Filas 3 a 6 del tablero, estas estan vacias
row3_6 = rowPair.verticalRepeat(2)

# La séptima fila del tablero (esta seria de peones blancos asi que solo alternamos la fila de peones negros
row7 = row2.negative()

# Octava fila con piezas blancas, alterna a la primera fila de piezas negras
row8 = row1.negative()

# Dibujamos el tablero completo donde la 1 esta por encima de todos y desciende hasta la 8
draw(row1.up(row2).up(row3_6).up(row7).up(row8))