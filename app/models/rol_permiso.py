from app.db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.models import rol, permiso

class Rol_permiso(db.Model):
    __tablename__="rols_permisos"
    id = Column(Integer,primary_key=True)
    permiso_id = Column(Integer, ForeignKey("permisos.id"))
    rol_id = Column(Integer, ForeignKey("rols.id"))
    permiso = relationship("Permiso", backref=backref("rols_permisos", cascade="all,delete-orphan"))
    rol = relationship("Rol",backref=backref("rols_permisos", cascade="all,delete-orphan"))

    def __init__(self, permiso_id, rol_id):
        self.permiso_id = permiso_id
        self.rol_id = rol_id
        db.session.commit()

    def add(permiso_id, rol_id):
        db.session.add(Rol_permiso(permiso_id, rol_id))
        db.session.commit()