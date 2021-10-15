from sqlalchemy import Column, Integer, String

from app.db import db

class Configuration(db.Model):
    
    __tablename__ = "configurations" 
    id = Column(Integer, primary_key=True)
    cant_filas = Column(Integer())
    order = Column(Integer())
    private_bg_color = Column(String(10))
    
    def __init__(self, cant_filas=None, order=None, private_bg_color="#FFFFAA"):
        self.cant_filas = cant_filas
        self.order = order
        self.private_bg_color = private_bg_color
    
    @classmethod
    def update(self, cant_filas=None, order=None, private_bg_color="#FFFFAA"):
        self.cant_filas = cant_filas
        self.order = order
        self.private_bg_color = private_bg_color
        db.session.commit()

    @classmethod
    def bg_color(self):
        return self.private_bg_color

    def get_id(self):
        return self.id