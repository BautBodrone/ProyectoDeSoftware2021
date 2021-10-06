from sqlalchemy import Column, Integer, String

from app.db import db

class Status(db.Model):
    
    __tablename__ = "statuses" 
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __init__(self, name=None):
        self.name = name
    
    def save(self, new_status):
        db.session.add(new_status)
        db.session.commit()