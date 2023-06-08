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
