from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  
  def __repr__(self):
    return f"<User {self.username}>"
  
  def guardaPassword( self , password):
    self.password = generate_password_hash(password)
    
  def comparaPassword(self ,password):
    return check_password_hash(self.password  , password)