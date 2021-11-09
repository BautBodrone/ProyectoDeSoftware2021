from app.db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.models import coordenada, punto

class Punto_coordenada(db.Model):
    __tablename__="punto_coordenada"
    id = Column(Integer,primary_key=True)
    punto_id = Column(Integer, ForeignKey("puntos.id"))
    coordenada_id = Column(Integer, ForeignKey("coordenadas.id"))

    def __init__(self, punto, coordenada):
        self.punto_id = punto
        self.coordenada_id = coordenada
        db.session.commit()

    def add(punto_id, coordenada_id):
        db.session.add(Punto_coordenada(punto_id, coordenada_id))
        db.session.commit()