from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db import db

from app.models import user_rol,rol

class User(db.Model):
    
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30),nullable=False)
    last_name = Column(String(30),nullable=False)
    email = Column(String(30),unique=True,nullable=False)
    password = Column(String(30),nullable=False)
    rols = relationship("Rol",secondary = "users_rols")
    activo = Column(Boolean)

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.activo = True

    @classmethod
    def get_email(self):
        return self.email
    
    @classmethod
    def authenticate_user(self, params):
        """
            Revisa en la base de datos para saber si se ingreso correctamente el email y la pass
            al logear
        """
        return self.query.filter(User.email==params["email"] and User.password==params["password"]).first()

    @classmethod
    def check_permiso(self, email, permiso):
        """
            Recive un email y un permiso y se fija si el usuario con ese email tiene ese permiso
        """
        user = db.session.query(User).filter_by(email=email).first()
        for rol in user.rols:
            for un_permiso in rol.permisos:
                if (un_permiso.nombre == permiso):
                    return True
        return False 

    @classmethod
    def check_rol(self, email, rol):
        """
            Recive un email y un permiso y se fija si el usuario con ese mail tiene ese rol
        """
        user = db.session.query(User).filter_by(email=email).first()
        for un_rol in user.rols:
            rol = un_rol.nombre
            if (un_rol.nombre == rol):
                return True
        return False 

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_user):
        db.session.add(new_user)
        db.session.commit()

    def search_user(id):
        return db.session.query(User).get(id)

    def search_user_email(email):
        return db.session.query(User).filter_by(email=email).first()

    def is_activo(self):
        return self.activo

    def edit(self,data):
        if self.first_name != data["first_name"]:
            self.first_name = data["first_name"]
        if self.last_name != data["last_name"]:
            self.last_name = data["last_name"]
        if self.password != data["password"]:
            self.password = data["password"]
        if self.email != data["email"]:
            self.email = data["email"]
        if data["estado"] == "True":
            aux = True
        else:
            aux = False
        if self.activo != aux:
            self.activo = aux
        db.session.commit()

    def search_email(unEmail):

        return db.session.query(User).filter_by(email=unEmail).first()
    
    def get_permisos(self):
        permisos = []
        for rol in self.rols:
            for permiso in rol.permisos:
                permisos.append(permiso)
        return permisos
