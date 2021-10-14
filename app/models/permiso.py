from sqlalchemy import Column, Integer, String
from app.db import db
from sqlalchemy.orm import relationship
from app.models.rol import Rol

rol_permiso = db.Table('tags',
    db.Column('rols', db.Integer, db.ForeignKey('rols.id'), primary_key=False),
    db.Column('permisos', db.Integer, db.ForeignKey('permisos.id'), primary_key=False)
)

class Permiso(db.Model):

    __tablename__ = 'permisos'
    id = Column(Integer,primary_key = True)
    nombre = Column(String(30))
    rols = relationship(Rol,secondary = rol_permiso, backref = db.backref('rols_p',lazy = 'dynamic'))
    
    def __init__(self,nombre = None):
        self.nombre = nombre
        db.session.commit()

    @classmethod 
    def save(self,new_permiso):
        db.session.add(new_permiso)
        db.session.commit()