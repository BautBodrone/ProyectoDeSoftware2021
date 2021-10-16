from sqlalchemy import Column, Integer, String

from app.db import db

class Configuration(db.Model):
    
    __tablename__ = "configurations" 
    id = Column(Integer, primary_key=True)
    cant_filas = Column(Integer())
    order = Column(Integer())
    private_bg_color = Column(String(10))
    private_accent_color = Column(String(10))
    private_letters_color = Column(String(10))
    public_bg_color = Column(String(10))
    public_accent_color = Column(String(10))
    public_letters_color = Column(String(10))
    
    def __init__(self, data):
        self.cant_filas = data["cant_filas"]
        self.order = data["order"]
        self.private_bg_color = data["private_bg_color"]
        private_accent_color = data["private_accent_color"]
        private_letters_color = data["private_letters_color"]
        public_bg_color = data["pubic_bg_color"]
        public_accent_color = data["public_accent_color"]
        public_letters_color = data["public_letters_color"]
    
    def update(self, data):
        if (data["cant_filas"] != '' and data["cant_filas"] != self.cant_filas):
            self.cant_filas = data["cant_filas"]
        if (data["order"] != self.order):
            self.order = data["order"]
        if (data["private_bg_color"] != self.private_bg_color):
            self.private_bg_color = data["private_bg_color"]
        if (data["private_accent_color"] != self.private_accent_color):
            self.private_accent_color = data["private_accent_color"]
        if (data["private_letters_color"] != self.private_letters_color):
            self.private_letters_color = data["private_letters_color"]
        if (data["public_bg_color"] != self.public_bg_color):
            self.public_bg_color = data["public_bg_color"]
        if (data["public_accent_color"] != self.public_accent_color):
            self.public_accent_color = data["public_accent_color"]
        if (data["public_letters_color"] != self.public_letters_color):
            self.public_letters_color = data["public_letters_color"]
        db.session.commit()

    def get_private_bg_color(self):
        return self.private_bg_color
    
    def get_private_accent_color(self):
        return self.private_accent_color

    def get_private_letters_color(self):
        return self.private_letters_color

    def get_public_bg_color(self):
        return self.public_bg_color

    def get_public_accent_color(self):
        return self.public_accent_color

    def get_public_letters_color(self):
        return self.public_letters_color
