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
    #denuncia = relationship("Denuncia", back_populates="seguimientos")
    #user = relationship("User", back_populates="seguimientos")
    fechaC = Column(Date)
    descripcion = Column(String(30))

    def __init__(self , titulo=None,descripcion=None,user=None,denuncia=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fechaC =  datetime.date.today()
        self.user =user
        self.denuncia =denuncia
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_seguimiento):
        db.session.add(new_seguimiento)
        db.session.commit()

    def edit(self,data):
        if self.titulo != data["titulo"]:
            self.titulo = data["titulo"]
        if self.descripcion != data["descripcion"]:
            self.descripcion = data["descripcion"]
        db.session.commit()