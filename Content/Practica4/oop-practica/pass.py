import random, string

class Pwd :

  def __init__ (self, longitud = 8):
    self.longitud = longitud
    if longitud > 0:
      self.contraseña = self.generarPwd()
    else:
      self.contraseña = "password"

  def generarPwd(self):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(self.longitud))
  
  

passw = Pwd(5)

print(passw.contraseña)