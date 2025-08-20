''' Escribe un programa que cree una clase para representar un objeto
punto en tres dimensiones.  
X - Y  - Z
Proporcionar un constructor que inicialice los
valores del punto al origen de coordenadas y otro que permita especificar las
coordenadas del punto. Sobrescribe su método __str__ para que muestre
información sobre los puntos. Usa la clase en un programa donde crees
objetos que representen los puntos (12, 13, 18) y (8, 14, 0) y los muestres por
consola.
'''

class punto :
  def __init__(self,x=0,y=0,z=0):
    self.x = x
    self.y = y
    self.z = z
  def __str__(self):
    return f'punto x = {self.x} | punto y = {self.y} | punto z = {self.z}'

punto1 = punto(12,12,12)
punto2 = punto()

print(punto1)
print(punto2)