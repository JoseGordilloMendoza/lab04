from colors import *

# Clase Picture que representa una imagen o figura
class Picture:
    # inicializar
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img
    # invertir color
  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]
    # espejo vertical
  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    vertical = self.img[::-1]
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    length = len(self.img[0])
    newimg = []

    for r in self.img:
      row = ""
      x = 0
      while x < length:
        row += r[length -1 -x]
        x += 1
      newimg.append(row)

    return Picture(newimg)
 # usamos la funcion anterior para invertir color y obtener el negativo
  def negative(self):
    """ Devuelve un negativo de la imagen """
    newimg = []

    for r in self.img:
      x = 0
      row = ""
      while x < len(r):
        row += self._invColor(r[x])
        x += 1
      newimg.append(row)

    return Picture(newimg)