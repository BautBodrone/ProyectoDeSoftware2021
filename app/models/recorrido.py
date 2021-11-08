from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

from app.models import coordenada,recorrido_coordenada
from app.db import db


class Recorrido(db.Model):

    ESTADOS = [
        ('publicado','Plublicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__ = "recorridos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True,nullable=False)
    descrpcion = Column(String(60))
    estado = Column(ChoiceType(ESTADOS))
    coordenadas = relationship("Coordenada", secondary="recorrido_coordenada")

    def __init__(self,nombre=None, descipcion=None, coordenadas=None, estado=None):
        self.nombre = nombre
        self.descrpcion = descipcion
        self.coordenadas = coordenadas
        self.estado = estado

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_recorrido):
        db.session.add(new_recorrido)
        db.session.commit()

    def edit(self,data):
        if self.nombre != data["nombre"]:
            self.nombre = data["nombre"]
        if self.descrpcion != data["descrpcion"]:
            self.descrpcion = data["descrpcion"]
        if self.coordenadas != data["coordenadas"]:
            self.coordenadas = data["coordenadas"]
        if self.estado != data["estado"]:
            self.estado = data["estado"]
        db.session.commit()
        