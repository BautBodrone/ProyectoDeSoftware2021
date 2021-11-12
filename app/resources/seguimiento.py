from flask import flash, redirect, render_template, request, url_for, session, abort
from app.models import denuncia
from app.models import seguimiento

from app.models.seguimiento import Seguimiento
from app.helpers.auth import authenticated
from app.db import db
from app.models.user import User

pagConf=4

def index():
    """
        El metodo mostrara todos las denuncias en una tabla
    """

    if not authenticated(session):
        abort(401)

    return render_template("seguimiento/index.html")

def new(denuncia):


    if not authenticated(session):
        abort(401)
    users = User.query.all()
    return render_template("Seguimiento/new.html", users=users,denuncia=denuncia)

def create():
    """
        El metodo ,si esta autenticado, creara una nueva denuncia
    """

    if not authenticated(session):
        abort(401)

    new_seguimiento = Seguimiento(**request.form)
    try:
        Seguimiento.save(new_seguimiento)
    except:
        flash("Denuncia con ese titulo o coordenadas ya existe", "error")
        return redirect(request.referrer)
    
    return redirect(url_for("seguimiento_index"))

def delete():
    """
        El metodo ,si esta autenticado, eliminara al usuario seleccionado
    """

    if not authenticated(session):
        abort(401)

    seguimiento = Seguimiento.search_denuncia(request.form["seguimiento_id"])
    seguimiento.delete()
    flash("Se elimino con exito")

    return redirect(url_for('seguimiento_index'))
