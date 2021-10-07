from sqlalchemy import Column, Integer, String
from app.db import db

class User(db.Model):
    
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30),unique=True)
    password = Column(String(30))

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    @classmethod
    def authenticate_user(self, params):
        return self.query.filter(User.email==params["email"] and User.password==params["password"]).first()
    
    @classmethod
    def save(self, new_user):
        db.session.add(new_user)
        db.session.commit()
    