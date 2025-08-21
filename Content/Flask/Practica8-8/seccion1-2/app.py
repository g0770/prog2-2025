from flask import Flask, request, render_template, redirect

class producto: #clase para seccion 2 ej 8
  def __init__(self,nombre:str,precio:float = 0):
    self.setNombre(nombre)
    self.setPrecio(precio)
  def getProducto(self):
    return {
      "nombre": self.nombre,
      "precio": self.precio
    }
  def setNombre(self, nombre:str):
    self.nombre = nombre
  def setPrecio(self, precio:float):
    self.precio = precio


app = Flask(__name__)

#seccion 1

@app.route("/")
def inicio():
  return "Hola, Mundo!"

@app.route("/saludo/<string:nombre>")
def saludo(nombre):
  return f"Hola {nombre}"

@app.route("/enviarnombre", methods=["GET", "POST"])
def enviarnombre():
  if request.method == "POST":
    nombre = request.form["nombre"]
    return f"Hola {nombre}"
  return '''<form method="post">
  Nombre: <input type="text" name="nombre">
  <input type="submit">
</form>
'''

@app.route("/enviaredad", methods=["GET", "POST"])
def enviaredad():
  if request.method == "POST":
    edad = request.form["edad"]
    return f"Hola {edad}"
  if request.method == "GET":
    return '''<form method="post">
  Edad: <input type="number" name="edad">
  <input type="submit">
</form>
'''

@app.route("/paroimpar/<int:numero>")
def paroimpar(numero):
  tipos = ("par","impar")
  return f"el numero {numero} es {tipos[numero%2]}"



#seccion 2

@app.route("/frutas")
def frutas():
  frutas = ("manzana", "durazno")
  return render_template("frutas.html", frutas = frutas)

@app.route("/productos")
def productos():
  productos = [producto("prod1",500),producto("prod1",50)]
  return render_template("productos.html", productos = productos)

@app.route("/welcome")
def welcome():
  return render_template("welcome.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  
  accounts = [{"usuario" : "admin", "contrasena" : "123"}, {"usuario" : "juan", "contrasena" : "newells"}]
  success = True
  
  if request.method == "POST":
    try:
      usuario = request.form["usuario"]
      contrasena = request.form["contrasena"]
      for i in accounts:
        if i["usuario"] == usuario and i["contrasena"] == contrasena:
          break
        success = False
    except Exception as e:
      print(e)
    if success:
      return render_template("loginSuccess.html", usuario = usuario)
    else:
      return render_template("login.html", success = success)
    
  elif request.method == "GET":
    return render_template("login.html", success = success)
  
  else:
    raise Exception(f"METODO NO SOPORTADO: {request.method}")

#todo buscar la manera de que en el html pueda tirar la funcion de una cuanto termine de cargar
#todo buscar la manera de que "success" cambie DONE MAYBE

#seccion 3
'''Sección 3: Bucles en Jinja2
11. Crear una página con un bucle que muestre los números del 1 al 10 en una lista
HTML.
12. Iterar sobre una lista de diccionarios en Jinja2: Mostrar una tabla con información
de productos (nombre, precio, categoría).
13. Generar una tabla de multiplicar para un número ingresado por el usuario a través
de un formulario.
14. Crear una página que muestre la lista de usuarios almacenados en una base de
datos utilizando SQLAlchemy (solo listar los usuarios).'''

@app.route("/bucle")
def bucle():
  return render_template("bucle.html")

@app.route("/listadiccionario")
def listadiccionario():
  accounts = [{"usuario" : "admin", "contrasena" : "123"}, {"usuario" : "juan", "contrasena" : "newells"}]
  return render_template("listadiccionario.html", accounts = accounts)


#seccion 4

pass



#seccion 5

pass



if __name__ == "__main__":
  app.run(debug=True)