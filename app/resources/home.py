from flask import render_template

from app.models.zona import Zona
from app.models.punto import Punto
from app.models.recorrido import Recorrido

# Ruta para el Home (usando decorator)
def index():

    recorridos = Recorrido.publicados()
    zonas = Zona.publicados()
    puntos = Punto.publicados()

    return render_template("home.html",zonas=zonas, puntos=puntos, recorridos=recorridos)