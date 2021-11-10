from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from app.db import db

zona_coordenada = Table("zonas_coordenadas",
    Column("zonas_id",ForeignKey("zonas.id")),
    Column("coordenadas_id",ForeignKey("coordenadas.id")))

class Zona(db.Model):

    __tablename__ = "zonas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    coordenadas = db.relationship("Coordenada", secondary="coordenadas", lazy='subquery',
        backref=db.backref('zonas', lazy=True))

    def __init__(self, nombre = None):
        self.nombre = nombre

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_zona):
        db.session.add(new_zona)
        db.session.commit()