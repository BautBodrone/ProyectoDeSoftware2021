from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import db
from app.models import coordenada, punto_coordenada
from sqlalchemy.orm import relationship

class Punto(db.Model):
    
    __tablename__ = "puntos" 
    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    nombre = Column(String(30), unique=True)
    coordenadas = relationship("Coordenada", secondary="punto_coordenada")
    estado = Column(String(30))
    telefono = Column(String(30))
    direccion = Column(String(30))

    def __init__(self, email=None, nombre=None, coordenadas=None, estado=None, telefono=None, direccion=None):
        self.email = email
        self.nombre = nombre
        self.coordenadas.append(coordenada.Coordenada.search_id(coordenadas))
        self.estado = estado
        self.telefono = telefono
        self.direccion = direccion

    def search_punto(id):
        """
            Retorna punto que tenga el mismo id que el que se paso por parametro
        """
        return db.session.query(Punto).get(id)
    
    @classmethod
    def save(self, new_punto):
        db.session.add(new_punto)
        print(db.session.commit())

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, punto):
        """
            Actualiza el punto con los valores pasados por parametro
        """
        self.nombre = punto["nombre"]
        self.direccion = punto["direccion"]
        self.coordenadas = punto["coordenadas"]
        self.estado = punto["estado"]
        self.telefono = punto["telefono"]
        self.email = punto["email"]
        db.session.commit()

    def to_dict(self):
        """
            Transforma los atributos del objeto en un diccionario
        """
        return {
            'nombre': self.nombre,
            'direccion': self.direccion,
            'coordenadas': self.coordenadas,
            'telefono': self.telefono,
            'estado': self.estado,
            'email': self.email,
            'id':self.id
        }