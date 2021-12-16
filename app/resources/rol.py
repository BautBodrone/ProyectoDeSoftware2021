from flask import render_template

from app.models.rol import Rol

def index():
    rols = Rol.query.all()

    return render_template("rol/index.html", rols=rols)