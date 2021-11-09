from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.rol import Rol
from app.helpers.auth import authenticated

def index():
    rols = Rol.query.all()

    return render_template("rol/index.html", rols=rols)