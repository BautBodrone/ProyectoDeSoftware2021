from sqlalchemy import Column, Integer, String
from app.db import db
from sqlalchemy.orm import relationship

from app.models import rol_permiso, rol

class Permiso(db.Model):

    __tablename__ = 'permisos'
    id = Column(Integer,primary_key = True)
    nombre = Column(String(30))
    rols = relationship("Rol",secondary = "rols_permisos")
    
    def __init__(self,nombre = None):
        self.nombre = nombre
        db.session.commit()

    @classmethod 
    def save(self,new_permiso):
        db.session.add(new_permiso)
        db.session.commit()     