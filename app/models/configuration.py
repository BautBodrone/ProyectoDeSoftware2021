from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType

from app.db import db

class Configuration(db.Model):
    
    CRITERIOS = [
        ('prioridad', 'Prioridad'),
        ('cercania', 'Cercania'),
        ('a..z', 'A..Z'),
        ('z..a', 'Z..A')
    ]

    __tablename__ = "configurations" 
    id = Column(Integer, primary_key=True)
    rows_per_page = Column(Integer(), default=10,nullable=False)
    order = Column(ChoiceType(CRITERIOS), default='a..z',nullable=False)
    private_bg_color = Column(String(10), default='#81AE9D',nullable=False)
    private_accent_color = Column(String(10), default='#21A179',nullable=False)
    private_letters_color = Column(String(10), default='#1E1E24',nullable=False)
    public_bg_color = Column(String(10), default='#81AE9D',nullable=False)
    public_accent_color = Column(String(10), default='#21A179',nullable=False)
    public_letters_color = Column(String(10), default='#1E1E24',nullable=False)
    
    def __init__(self, data):
        self.rows_per_page = data["rows_per_page"]
        self.order = data["order"]
        self.private_bg_color = data["private_bg_color"]
        self.private_accent_color = data["private_accent_color"]
        self.private_letters_color = data["private_letters_color"]
        self.public_bg_color = data["pubic_bg_color"]
        self.public_accent_color = data["public_accent_color"]
        self.public_letters_color = data["public_letters_color"]
    
    def update(self, data):
        """
            Actualiza los valores si son distintos a los pasados por parametro
        """
        if (data["rows_per_page"] != '' and data["rows_per_page"] != self.rows_per_page):
            self.rows_per_page = data["rows_per_page"]
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
        """
            Retorna el valor de private_bg_color
        """
        return self.private_bg_color
    
    def get_private_accent_color(self):
        """
            Retorna el valor de private_accent_color
        """
        return self.private_accent_color

    def get_private_letters_color(self):
        """
            Retorna el valor de private_letter_color
        """
        return self.private_letters_color

    def get_public_bg_color(self):
        """
            Retorna el valor de publi_bg_color
        """
        return self.public_bg_color

    def get_public_accent_color(self):
        """
            Retorna el valor de public_accent_color
        """
        return self.public_accent_color

    def get_public_letters_color(self):
        """
            Retorna el valor de public_letters_color
        """
        return self.public_letters_color

    def get_rows_per_page(self):
        """
            Retorna el valor de elementos por pagina
        """
        return self.rows_per_page

    def get_config():
       """
            Retorna el objeto configurations
       """
       return db.session.query(Configuration).first()