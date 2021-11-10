from app.db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.models import coordenada, recorrido

class Recorrido_coordenada(db.Model):
    __tablename__="recorrido_coordenada"
    id = Column(Integer,primary_key=True)
    recorrido_id = Column(Integer, ForeignKey("recorridos.id"))
    coordenada_id = Column(Integer, ForeignKey("coordenadas.id"))
    
    def __init__(self, recorrido, coordenada):
        self.recorrido_id = recorrido
        self.coordenada_id = coordenada
        db.session.commit()

    def add(recorrido_id, coordenada_id):
        db.session.add(Recorrido_coordenada(recorrido_id, coordenada_id))
        db.session.commit()