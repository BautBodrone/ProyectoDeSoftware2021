from sqlalchemy import Column, Integer, String

from app.db import db

class Configuration(db.Model):
    
    __tablename__ = "configurations" 
    id = Column(Integer, primary_key=True)
    cant_filas = Column(Integer())
    order = Column(Integer())
    
    def __init__(self, cant_filas=None, order=None):
        self.cant_filas = cant_filas
        self.order = order
    
    @classmethod
    def save(self, new_config):
        db.session.add(new_config)
        db.session.commit()