from flask import Flask, request, render_template, redirect, url_for, session
from models.user import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:gotto@localhost/logintest"
app.config["SECRET_KEY"] = "5b36cdc9b28dae7d1e15b99a62fb5092a4a9189438ceac54f7739f4c68ab4c8b"
#para la key, python -c 'import secrets; print(secrets.token_hex())'    (en consola)
#obviamente no tendria que estar en el repositorio pero bueno es para testear
db.init_app(app)

'''@app.before_first_request # DEPRECATED
def create_tables():
  db.create_all()''' 
  
# https://stackoverflow.com/questions/73570041/flask-deprecated-before-first-request-how-to-update
# https://flask.palletsprojects.com/en/stable/quickstart/
# https://flask.palletsprojects.com/en/stable/quickstart/#sessions

_firstBoot = True 
@app.before_request
def start():
  global _firstBoot
  if _firstBoot:
    print("First boot")
    _firstBoot = False
    db.create_all()
    

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
  success = True
  if request.method == "POST":
    try:
      username = request.form["username"]
      password = request.form["password"]
      user = User.query.filter_by(username=username,password=password).first()
      if not user:
        success = False
        return redirect(url_for("login")) #automaticamente es get xq es codigo metodo 303
      else:
        session["username"] = user.username
        session["password"] = user.password
        return redirect(url_for("home"))
    except Exception as e:
      print(e)    
  elif request.method == "GET":
    return render_template("login.html", success = success)  
  else:
    raise Exception(f"METODO NO SOPORTADO: {request.method}")
  

@app.route("/home")
def home():
  return render_template("home.html", username = session["username"])

if __name__ == "__main__":
  app.run(debug=True)