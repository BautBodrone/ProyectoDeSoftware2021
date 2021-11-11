from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import db


class Puntos(db.Model):
    
    __tablename__ = "puntosDeEncuentro" 
    id = Column(Integer, primary_key=True)
    email = Column(String(30),nullable=False)
    nombre = Column(String(30), unique=True,nullable=False)
    coordenadas = Column(String(30), unique=True,nullable=False)
    estado = Column(String(30),nullable=False)
    telefono = Column(String(30),nullable=False)
    direccion = Column(String(30),nullable=False)

    def __init__(self, email=None, nombre=None, coordenadas=None, estado=None, telefono=None, direccion=None):
        self.email = email
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.estado = estado
        self.telefono = telefono
        self.direccion = direccion

    def search_punto(id):
        return db.session.query(Puntos).get(id)
    
   

    @classmethod
    def save(self, new_punto):
        db.session.add(new_punto)
        print(db.session.commit())

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, punto):
        self.nombre = punto["nombre"]
        self.direccion = punto["direccion"]
        self.coordenadas = punto["coordenadas"]
        self.estado = punto["estado"]
        self.telefono = punto["telefono"]
        self.email = punto["email"]
        db.session.commit()

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'direccion': self.direccion,
            'coordenadas': self.coordenadas,
            'telefono': self.telefono,
            'estado': self.estado,
            'email': self.email,
            'id':self.id
        }

    
    

        
