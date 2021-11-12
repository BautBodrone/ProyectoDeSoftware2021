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
        return db.session.query(Zona).get(id)
        
    def publicados():
        try:
            return db.session.query(Recorrido).filter_by(estado='Publicado').all()
        except:
            return []