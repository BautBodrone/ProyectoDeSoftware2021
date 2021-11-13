from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import db
from sqlalchemy_utils import ChoiceType

from app.db import db

class Recorrido(db.Model):

    ESTADOS = [
        ('publicado','Publicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__ = "recorridos"
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(30), unique=True,nullable=False)
    descripcion = db.Column(String(60))
    estado = db.Column(ChoiceType(ESTADOS))
    coordenadas = db.Column(db.String(255), nullable=False)

    def __init__(self,nombre=None, descripcion=None, coordenadas=None, estado=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.coordenadas = coordenadas
        self.estado = estado

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_recorrido):
        db.session.add(new_recorrido)
        db.session.commit()

    def edit(self,data):
        self.nombre = data["nombre"]
        self.descripcion = data["descripcion"]
        self.coordenadas = data["coordenadas"]
        self.estado = data["estado"]
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_recorrido):
        db.session.add(new_recorrido)
        db.session.commit()

    def search_id(id):
        return db.session.query(Recorrido).get(id)
        
    def publicados():
        try:
            return db.session.query(Recorrido).filter_by(estado='Publicado').all()
        except:
            return []
        
    def update(self, recorrido):
        """
            Actualiza el zona con los valores pasados por parametro
        """
        if self.nombre != recorrido["nombre"]:
            self.nombre = recorrido["nombre"]
        if self.estado != recorrido["estado"]:    
            self.estado = recorrido["estado"]
        if self.descripcion != recorrido["descripcion"]:
            self.descripcion = recorrido["descripcion"]
        if self.coordenadas != recorrido["coordenadas"]:
            self.coordenadas = recorrido["coordenadas"]
        db.session.commit()