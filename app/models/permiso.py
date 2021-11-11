from sqlalchemy import Column, Integer, String
from app.db import db

class Permiso(db.Model):

    __tablename__ = 'permisos'
    id = Column(Integer,primary_key = True)
    nombre = Column(String(30))
    descripcion = Column(String(255))
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        db.session.commit()

    @classmethod 
    def save(self,new_permiso):
        db.session.add(new_permiso)
        db.session.commit()     