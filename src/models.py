import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_de_subscripcion = Column(String(250), nullable=False)
    usuario = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates = "usuario")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    altura = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    color_cabello = Column(String(250), nullable=False)
    color_ojos = Column(String(250), nullable=False)
    edad = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates = "personaje")

    def to_dict(self):
        return {}

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    diametro = Column(String(250), nullable=False)
    periodo_rotacion = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates = "planeta")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    planeta_id = Column(Integer, ForeignKey("planetas.id"))
    usuario = relationship("Usuario", back_populates = "favoritos")
    planeta = relationship("Planeta", back_populates = "favoritos")
    personaje = relationship("Personaje", back_populates = "favoritos")
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
