# Constantes para representar colores en RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (200, 200, 200)
GRAY = (127, 127, 127)
DARKGRAY = (50, 50, 50)
BLUE = (0, 0, 255)
 
# "color" sirve para mapear símbolos a colores
color = {
  '_': LIGHTGRAY,  # Símbolo '_' representa el color LIGHTGRAY
  '=': GRAY,       # Símbolo '=' representa el color GRAY
  '.': WHITE,      # Símbolo '.' representa el color WHITE
  '@': BLACK,      # Símbolo '@' representa el color BLACK
  '#': DARKGRAY,   # Símbolo '#' representa el color DARKGRAY
  ' ': BLUE,       # Símbolo ' ' representa el color BLUE
}

# "inverter" mapea símbolos a sus inversos
inverter = {
  '_': '=',   # Símbolo '_' tiene el inverso '='
  '=': '_',   # Símbolo '=' tiene el inverso '_'
  '.': '@',   # Símbolo '.' tiene el inverso '@'
  '@': '.',   # Símbolo '@' tiene el inverso '.'
}