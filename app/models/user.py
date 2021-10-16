from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db import db

from app.models import user_rol,rol

class User(db.Model):
    
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30),unique=True)
    password = Column(String(30))
    rols = relationship("Rol",secondary = "users_rols")
    

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @classmethod
    def get_email(self):
        return self.email
    
    @classmethod
    def authenticate_user(self, params):
        return self.query.filter(User.email==params["email"] and User.password==params["password"]).first()

    @classmethod
    def check_permiso(self, email, permiso):
        user = db.session.query(User).filter_by(email=email).first()
        for rol in user.rols:
            permisos = rol.permisos
            for unPermiso in permisos:
                if (unPermiso.nombre == permiso):
                    return True
        return False 

    @classmethod
    def check_rol(self,rol):
        if self.user_r() is None:
            print('testing')
            return True
        else:
            for rol_s in self.user_r():
                if rol_s == rol:
                    return True
            return False

    @classmethod
    def add_rol(cls,rol):
        if check_rol(rol):
            return False
        else:
            #add rol
            return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod 
    def save(self, new_user):
        db.session.add(new_user)
        db.session.commit()

    def search_user(id):
        return db.session.query(User).get(id)

    def edit(self,data):
        if self.first_name != data["first_name"]:
            self.first_name = data["first_name"]
        if self.last_name != data["last_name"]:
            self.last_name = data["last_name"]
        if self.password != data["password"]:
            self.password = data["password"]
        if self.email != data["email"]:
            self.email = data["email"]
        db.session.commit()

    def search_email(unEmail):

        return db.session.query(User).filter_by(email=unEmail).first()
    