from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.sql.schema import ForeignKey 
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from app.models.user import User
import datetime 
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship, backref

class Denuncia(db.Model):

    ESTADOS = [
        ('sinConfirmar','Sin Confirmar'),
        ('curso','Curso'),
        ('resuelta','Resuelta'),
        ('cerrada','Cerrada')
    ]

    CATEGORIAS = [
        ('cañeria_rota','Cañeria Rota'),
        ('calle_inundable','Calle Inundable'),
        ('calle_rota','Calle rota'),
        ('otro','Otro')
    ]
    
    __tablename__ = "denuncias" 
    id = Column(Integer, primary_key=True)
    titulo = Column(String(30),unique=True)
    categoria = Column(ChoiceType(CATEGORIAS))
    fechaC = Column(Date)
    fechaF = Column(Date)
    descripcion = Column(Text)
    lat = Column(String(30))    
    lng = Column(String(30))
    estado = Column(ChoiceType(ESTADOS))
    apellidoD = Column(String(30))
    nombreD = Column(String(30))
    telefono = Column(String(30))
    emailD = Column(String(30))
    asignadoA_id = Column(Integer, ForeignKey('users.id'))
    seguimientos = relationship('Seguimiento', backref='denuncia', lazy=True)

    def __init__(self , titulo,categoria,descripcion,
                    lat,lng,estado,apellidoD 
                    ,nombreD,telefono ,emailD,asignadoA=None):
        self.titulo = titulo
        self.categoria = categoria
        self.descripcion = descripcion
        self.lat = lat
        self.lng = lng
        self.fechaC =  datetime.date.today()
        self.fechaF = None
        self.estado = estado
        self.apellidoD = apellidoD
        self.nombreD = nombreD
        self.telefono = telefono
        self.emailD = emailD
        self.asignadoA_id=asignadoA

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_denuncia):
        db.session.add(new_denuncia)
        db.session.commit()


    def search_denuncia(id):
        return db.session.query(Denuncia).get(id)

    def estado_denuncia(self):
        return self.estado

    def edit(self,data):
        if self.titulo != data["titulo"]:
            self.titulo = data["titulo"]

        if self.categoria != data["categoria"]:
            self.categoria = data["categoria"]

        if self.estado == "cerrada":
            if self.fechaF != data["fechaF"]:
                self.fechaF = data["fechaF"]

        if self.descripcion != data["descripcion"]:
            self.descripcion = data["descripcion"]

        if self.lat != data["lat"]:
            self.lat = data["lat"]

        if self.lng != data["lng"]:
            self.lng = data["lng"]

        if self.estado != data["estado"]:
            self.estado = data["estado"]

        if self.apellidoD != data["apellidoD"]:
            self.apellidoD = data["apellidoD"]

        if self.nombreD != data["nombreD"]:
            self.nombreD = data["nombreD"]

        if self.telefono != data["telefono"]:
            self.telefono = data["telefono"]

        if self.emailD != data["emailD"]:
            self.emailD = data["emailD"]

        if self.estado == "cerrada" and self.fechaF == None:
            self.fechaF = datetime.date.today()
        db.session.commit()