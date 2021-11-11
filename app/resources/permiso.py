from app.models.permiso import Permiso
from flask import render_template

def index():
    """
        Solo para crear la tabla
    """
    permisos = Permiso.query.all()

    return render_template("permiso/index.html", permisos=permisos)