from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.schema import ForeignKey 
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import relationship
from app.db import db
import datetime 

class Seguimiento(db.Model):

    __tablename__ = "seguimientos" 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    denuncia_id = Column(Integer, ForeignKey('denuncias.id'))
    fechaC = Column(Date)
    descripcion = Column(Text)

    def __init__(self,denuncia_id,descripcion=None,user=None):
        self.descripcion = descripcion
        self.fechaC =  datetime.date.today()
        self.user_id = user
        self.denuncia_id = denuncia_id
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_seguimiento):
        db.session.add(new_seguimiento)
        db.session.commit()
