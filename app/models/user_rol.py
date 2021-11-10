from app.db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.models import user, rol

class User_rol(db.Model):
    __tablename__="users_rols"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    rol_id = Column(Integer, ForeignKey("rols.id"))
    user = relationship("User")
    rol = relationship("Rol")

    def __init__(self, user_id, rol):
        self.user_id = user_id
        self.rol_id = rol
        db.session.commit()

    def add(user_id, rol_id):
        db.session.add(User_rol(user_id, rol_id))
        db.session.commit()