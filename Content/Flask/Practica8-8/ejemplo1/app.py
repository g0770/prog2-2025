from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def inicio():
  return "Hola mundo"

@app.route("/test")
def test():
  return render_template("test.html")

@app.route("/testint/<int:num>")
def testint(num):
  #return f"numero: {num}"
  return render_template("testint.html",num=num)

@app.route("/teststr/<string:str>")
def teststr(str):
  #return f"str: {str}"
  return render_template("teststr.html",str=str)

@app.route("/testsuma/<int:n1>/<int:n2>")
def testsuma(n1, n2):
  #return f"suma: {n1 + n2}"
  return render_template("testsuma.html",suma=n1+n2)

@app.route("/testform", methods=["GET","POST"])
def testform():
  if request.method == "POST":
    nombre = request.form["nombre"]
    return f"Hola {nombre}, recibí tu formulario"
  return render_template("testform.html")

@app.route("/rickroll")
def rickroll():
  return redirect(location="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == "__main__":
  app.run(debug=False)