from sqlalchemy import Column, String
from sqlalchemy.sql.schema import UniqueConstraint
from app.db import db
from sqlalchemy_utils import ChoiceType


class Punto(db.model):

    ESTADOS = [
        ('publicado','Plublicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__= 'puntos'
    nombre = Column(String (30))
    direccion = Column(String(30))
    coordenadas1 = Column(String(30))
    estado = Column(ChoiceType(ESTADOS))
    telefono = Column(String(20))
    email = Column(String(30))
    
    __table_args__ = (UniqueConstraint('nombre','direccion', name = '_punto_uc'))

    def __init__(self,nombre = None, direccion = None, coordenadas1 = None, estado = None,telefono = None,email = None):
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas1 = coordenadas1
        self.estado = estado
        self.telefono = telefono
        self.email = email

    @classmethod 
    def save(self, new_punto):
        db.session.add(new_punto)
        db.session.commit()
    