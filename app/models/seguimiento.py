from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey 
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from app.db import db
import datetime 
from sqlalchemy_utils import ChoiceType

class Seguimiento(db.Model):

    __tablename__ = "seguimientos" 
    id = Column(Integer, primary_key=True)
    denuncia_id= Column(Integer,ForeignKey('denuncia.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    fechaC = Column(Date)
    descripcion = Column(String(30))

    def __init__(self , titulo=None,descripcion=None,userId=None,denuncia_id=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fechaC =  datetime.date.today()
        self.userId =userId
        self.denuncia_id =denuncia_id
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_denuncia):
        db.session.add(new_denuncia)
        db.session.commit()

    def edit(self,data):
        if self.titulo != data["titulo"]:
            self.titulo = data["titulo"]
        if self.descripcion != data["descripcion"]:
            self.descripcion = data["descripcion"]
        db.session.commit()