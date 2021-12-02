from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.sql.expression import false
from app.db import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.rol import Rol


user_rol = db.Table("users_rols",db.Column("users_id",db.ForeignKey("users.id")),db.Column("rols_id",db.ForeignKey("rols.id")))

class User(db.Model):
    
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)

    rols = db.relationship("Rol",secondary = user_rol, lazy='subquery',backref=db.backref('users', lazy=True))
    first_name = Column(String(30),nullable=False)
    last_name = Column(String(30),nullable=False)
    email = Column(String(30),unique=True,nullable=False)
    username = Column(String(30),unique=True,nullable=False)
    password = Column(Text,nullable=False)
    activo = Column(Boolean)
    denuncias = relationship('Denuncia', backref='asignadoA', lazy=True)
    seguimientos = relationship('Seguimiento', backref='user', lazy=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None, username=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        self.activo = True
        self.username = username
        self.rols.append(Rol.search("operador"))
        

    @classmethod
    def get_email(self):
        return self.email
    
    @classmethod
    def authenticate_user(self, params):
        """
            Revisa en la base de datos para saber si se ingreso correctamente el email y la pass
            al logear
        """
        aux=self.query.filter(User.username==params["username"]).first()
        try:
            check=check_password_hash(aux.password,params["password"])
        except AttributeError:
            check = False
        if check:
            return aux
        else:
            return None

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


    def get(user_email):
        ######## retornar valores del user
        
        return ("first_name","last_name","email","username","password" ,"activo")

    def is_activo(self):
        return self.activo

    def edit(self,data):
        if self.username != data ["username"]:
            self.username = data["username"]
        if self.first_name != data["first_name"]:
            self.first_name = data["first_name"]
        if self.last_name != data["last_name"]:
            self.last_name = data["last_name"]
        aux=self.query.filter(User.email==data["email"]).first()
        if not check_password_hash(aux.password,data["password"]):
            self.password = generate_password_hash(data["password"])
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
