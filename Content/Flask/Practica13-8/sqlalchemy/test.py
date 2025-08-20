from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

#engine = create_engine("sqlite:///basedatos.db", echo=True)
engine = create_engine("mysql+pymysql://usuario:clave@localhost/nombre_bd")

Base = declarative_base()

class Usuario(Base):
  __tablename__ = "usuarios"
  id = Column(Integer, primary_key = True)
  nombre = Column(String(50))
  email = Column(String(100))
  clave = Column(String(100))