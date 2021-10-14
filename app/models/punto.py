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
    
    id = Column(Integer, primary_key=True) 
    nombre = Column(String (30))
    direccion = Column(String(30))
    coordenadas1 = Column(String(30), unique=True)
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

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def search_punto(p_id):
        return db.session.query(Punto).get(p_id)

    def edit(self, data):
        if self.nombre != data["nombre"]:
            self.nombre = data["nombre"]
        if self.direccion != data["direccion"]:
            self.direccion = data["direccion"]
        if self.coordenadas1 != ["coordenadas1"]:
            self.coordenadas1 = data["coordenadas1"]
        if self.estado != data["estado"]:
            self.estado = data["estado"]
        if self.telefono != data["telefono"]:
            self.telefono = data["telefono"]
        if self.email != data["email"]:
            self.email = data["email"]
        db.session.commit()

