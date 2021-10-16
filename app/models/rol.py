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

    def __init__(self,nombre = None):
        self.nombre = nombre

    @classmethod 
    def check_permiso(cls, self, permiso):
        if(self.rols_p() is None):
            print('testing no tiene nada')
        else:
            for permiso_self in self.rols_p():
                if (permiso_self == permiso):
                    return True
            return False

    @classmethod 
    def save(self,new_rol):
        db.session.add(new_rol)
        db.session.commit()