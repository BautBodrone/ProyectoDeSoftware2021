from sqlalchemy.orm import defaultload
from app.db import db
from sqlalchemy_utils import ChoiceType
from app.models.coordenada import Coordenada

zona_coordenada = db.Table("zonas_coordenadas",db.Column("zonas_id",db.ForeignKey("zonas.id")),db.Column("coordenadas_id",db.ForeignKey("coordenadas.id")))

class Zona(db.Model):

    ESTADOS = [
        ('publicado','Plublicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__ = "zonas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    estado = db.Column(ChoiceType(ESTADOS),nullable=False)
    color = db.Column(db.String(10), default="#FF6E4E",nullable=False)
    coordenadas = db.relationship("Coordenada", secondary=zona_coordenada, lazy='subquery',backref=db.backref('zonas', lazy=True))

    def __init__(self, nombre = None, estado = None, color = None, coordenadas = None):
        self.nombre = nombre
        self.estado = estado
        self.color = color
        for coordenada in coordenadas:
            self.coordenadas.append(Coordenada.search_id(coordenada))

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_zona):
        db.session.add(new_zona)
        db.session.commit()

    def search_id(id):
        return db.session.query(Zona).get(id)
