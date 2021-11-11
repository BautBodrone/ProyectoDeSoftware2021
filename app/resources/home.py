from flask import render_template

from app.models.zona import Zona
from app.models.punto import Punto

# Ruta para el Home (usando decorator)
def index():
    
    zonas = Zona.query.all()
    puntos = Punto.publicados()

    return render_template("home.html",zonas=zonas, puntos=puntos)