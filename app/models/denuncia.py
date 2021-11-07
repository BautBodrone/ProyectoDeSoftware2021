from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from app.db import db
import datetime 

class Denuncia(db.Model):
    
    __tablename__ = "denuncias" 
    id = Column(Integer, primary_key=True)
    titulo = Column(String(30),unique=True)
    categoria = Column(String(30))
    fechaC = Column(Date)
    fechaF = Column(Date)
    descripcion = Column(String(30))
    coordenadas = Column(String(30))
    estado = Column(String(30))
    apellidoD = Column(String(30))
    nombreD = Column(String(30))
    telefono = Column(String(30))
    emailD = Column(String(30))
    

    def __init__(self , titulo=None,categoria=None,descripcion=None,
                    coordenadas=None,estado=None,apellidoD=None ,nombreD=None,telefono=None ,emailD=None):
        self.titulo = titulo
        self.categoria = categoria
        self.descripcion = descripcion
        self.coordenadas = coordenadas
        self.fechaC =  datetime.date.today()
        self.fechaF = null
        self.estado = estado
        self.apellidoD = apellidoD
        self.nombreD = nombreD
        self.telefono = telefono
        self.emailD = emailD

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
        if self.fechaC != data["fechaC"]:
            self.fechaC = data["fechaC"]
        if self.descripcion != data["descripcion"]:
            self.descripcion = data["descripcion"]
        if self.coordenadas != data["coordenadas"]:
            self.coordenadas = data["coordenadas"]
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
        if "cerrado" == data["fechaF"]:
            self.fechaF = datetime.date.today()
        db.session.commit()

    def print(self):
        print("id =", self.id)
        print("titulo =", self.titulo)
        print("categoria =", self.categoria)
        print("fechaC =", self.fechaC)
        print("fechaF =", self.fechaF)
        print("descripcion =", self.descripcion)
        print("coordenadas =", self.coordenadas)
        print("estado =", self.estado)
        print("apellidoD =", self.apellidoD)
        print("nombreD =", self.nombreD)
        print("telefono =", self.telefono)
        print("emailD =", self.emailD)