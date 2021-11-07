from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import db

class Coordenada(db.Model):

    __table_args__ = (db.UniqueConstraint("latutid","longitud"),)

    __tablename__ = "coordenadas"
    id = Column(Integer,primary_key=True)
    latitud = Column(String)
    longitud = (Column(String))

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