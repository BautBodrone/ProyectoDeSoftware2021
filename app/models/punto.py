from sqlalchemy import Column, String, Integer
from sqlalchemy import PrimaryKeyConstraint,UniqueConstraint
from app.db import db
from sqlalchemy_utils import ChoiceType

class Punto(db.Model):
    

    ESTADOS = [
        ('publicado','Plublicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__= "puntos"
    
    #id = Column(Integer, primary_key=True) # solo es testing
    nombre = Column(String (30))
    direccion = Column(String(30))
    coordenadas1 = Column(String(30), primary_key=True)
    estado = Column(ChoiceType(ESTADOS))
    telefono = Column(String(20))
    email = Column(String(30))
    

    def __init__(self,nombre = None, direccion = None, coordenadas1 = None, estado = None,telefono = None,email = None):
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas1 = coordenadas1
        self.estado = estado
        self.telefono = telefono
        self.email = email

    @classmethod 
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def save(self, new_punto):
        db.session.add(new_punto)
        db.session.commit()

    def search_punto(p_coordenadas):
        return db.session.query(Punto).filter_by(nombre=p_coordenadas).first()

