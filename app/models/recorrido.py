from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy_utils import ChoiceType

from app.models import coordenada
from app.db import db

coordenadas = db.Table('recorridos_coordenadas',
    db.Column('recorrido_id', db.Integer, db.ForeignKey('recorrdio.id'), primary_key=True),
    db.Column('coordenada_id', db.Integer, db.ForeignKey('coordenada.id'), primary_key=True)
)

class Recorrido(db.Model):

    ESTADOS = [
        ('publicado','Plublicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__ = "recorridos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True,nullable=False)
    descrpcion = Column(String(60))
    coordenadas = db.relationship("Coordenada", secondary=coordenadas)
    estado = Column(ChoiceType(ESTADOS))

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
        