from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.category import Category
from app.models.status import Status
from app.db import db

class Issue(db.Model):
    
    __tablename__ = "issues" 
    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    description = Column(String(30))
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)
    status_id = Column(Integer,ForeignKey("statuses.id"))
    status = relationship(Status)

    def __init__(self, email=None, description=None, status_id=None, category_id=None):
        self.email = email
        self.description = description
        self.status_id = status_id
        self.category_id = category_id

    @classmethod
    def save(self, new_issue):
        db.session.add(new_issue)
        db.session.commit()
