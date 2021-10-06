from sqlalchemy import Column, Integer, String

from app.db import db

class Category(db.Model):
    
    __tablename__ = "categories" 
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __init__(self, name=None):
        self.name = name
    
    def save(self, new_category):
        db.session.add(new_category)
        db.session.commit()
    