from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import db

user_rol = db.Table('tags',
    db.Column('rols', db.Integer, db.ForeignKey('rols.id'), primary_key=False),
    db.Column('users', db.Integer, db.ForeignKey('usersS.id'), primary_key=False)
)

class Rol(db.Model):

    __tablename__ = 'rols'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(30))
    users = relationship('User',secondary = user_rol, backref = db.backref('users_r',lazy = 'dynamic'))
    
    def __init__(self,nombre = None):
        self.nombre = nombre

    @classmethod 
    def check_permiso(cls, permiso):
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