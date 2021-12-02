from sqlalchemy import Column, Integer, String
from app.db import db

rol_permiso = db.Table("rols_permisos",db.Column("rols_id",db.ForeignKey("rols.id")),db.Column("permisos_id",db.ForeignKey("permisos.id")))

class Rol(db.Model):

    __tablename__ = 'rols'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(30))
    permisos = db.relationship("Permiso",secondary = rol_permiso, lazy='subquery',backref=db.backref('rols', lazy=True))

    def __init__(self,nombre):
        self.nombre = nombre

    def check_permiso(self, permiso):
        """
            Retorna verdadero o falso dependiendo si el rol tiene el permiso pasado
            por parametro
        """
        for un_permiso in self.permisos:
            if (un_permiso.nombre == permiso):
                return True
        return False 

    @classmethod 
    def save(self,new_rol):
        db.session.add(new_rol)
        db.session.commit()
        
    def search(nombre):
        """
            Busca un rol por nobre
        """
        return db.session.query(Rol).filter_by(nombre=nombre).first()
