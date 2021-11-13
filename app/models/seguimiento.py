from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey 
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import relationship
from app.db import db
import datetime 

class Seguimiento(db.Model):

    __tablename__ = "seguimientos" 
    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    denuncia = Column(Integer)
    fechaC = Column(Date)
    descripcion = Column(String(80))

    def __init__(self ,descripcion=None,user=None):
        self.descripcion = descripcion
        self.fechaC =  datetime.date.today()
        self.user =user
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_seguimiento):
        db.session.add(new_seguimiento)
        db.session.commit()
