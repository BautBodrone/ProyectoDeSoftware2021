from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.db import db
from app.models import punto_coordenada, recorrido_coordenada

class Coordenada(db.Model):

    __table_args__ = (db.UniqueConstraint("latitud","longitud"),)

    __tablename__ = "coordenadas"
    id = Column(Integer,primary_key=True)
    latitud = Column(String(30),nullable=False)
    longitud = Column(String(30),nullable=False)
    recorridos = db.relationship("Recorrido", secondary="recorrido_coordenada")
    puntos = relationship("Punto", secondary="punto_coordenada")

    def __init__(self,latitud,longitud):
        self.latitud = latitud
        self.longitud = longitud

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_user):
        db.session.add(new_user)
        db.session.commit()

    def edit(self,data):
        if self.latitud != data["latitud"]:
            self.latitud = data["latitud"]
        if self.longitud != data["lonitud"]:
            self.longitud = data["longitud"]
        db.session.commit()

    def search_coordenada(id):
        return db.session.query(Coordenada).get(id)