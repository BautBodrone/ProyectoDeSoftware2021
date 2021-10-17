from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.rol import Rol
from app.helpers.auth import authenticated

'El metodo mostrara todos los roles con sus permisos'
def index():
    rols = Rol.query.all()

    return render_template("rol/index.html", rols=rols)