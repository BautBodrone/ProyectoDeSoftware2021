from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import db

from app.models import permiso, user

class Rol(db.Model):

    __tablename__ = 'rols'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(30))
    users = relationship("User",secondary = "users_rols")
    permisos = relationship("Permiso",secondary = "rols_permisos")

    def __init__(self,nombre):
        self.nombre = nombre

    def check_permiso(self, permiso):
        """
            Retorna verdadero o falso dependiendo si el rol tiene el permiso pasado
            por parametro
        """
        for un_permiso in self.permisos:
            if (un_permiso.nombre == permiso):
                return True
        return False 

    @classmethod 
    def save(self,new_rol):
        db.session.add(new_rol)
        db.session.commit()
