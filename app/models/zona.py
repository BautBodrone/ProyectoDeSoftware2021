from sqlalchemy.orm import defaultload
from app.db import db
from sqlalchemy_utils import ChoiceType

class Zona(db.Model):

    ESTADOS = [
        ('publicado','Publicado'),
        ('despublicado','Despublicado')
    ]

    __tablename__ = "zonas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=False)
    estado = db.Column(ChoiceType(ESTADOS),nullable=False)
    color = db.Column(db.String(10), default="#FF6E4E",nullable=False)
    coordenadas = db.Column(db.Text, nullable=False)

    def __init__(self, nombre, estado, coordenadas, color = "#FF6E4E"):
        self.nombre = nombre
        self.estado = estado
        self.color = color
        self.coordenadas = coordenadas

    def update(self,zona):
        """
            Actualiza la zona con los valores pasados por parametro
        """
        self.nombre = zona["nombre"]
        self.estado = zona["estado"]
        self.color = zona["color"]
        self.coordenadas = zona["zonas"]
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_zona):
        db.session.add(new_zona)
        db.session.commit()

    @classmethod
    def search_id(cls,id):
        return db.session.query(Zona).get(id)

    @classmethod
    def publicados(cls):
        try:
            return db.session.query(Zona).filter_by(estado='publicado').all()
        except:
            return []
    
    @classmethod
    def upload(cls,zona):
        aux = db.session.query(Zona).filter_by(nombre=zona["nombre"]).first()
        try:
            if( aux != None):
                aux.update(zona)
            else:
                Zona.save(zona)
        except:
            raise 
        