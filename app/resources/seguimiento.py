from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.seguimiento import Seguimiento
from app.helpers.auth import authenticated
from app.db import db
from app.models.user import User

pagConf=4

def denuncia(unaDenuncia):
    denuncia=unaDenuncia


def index(denuncia_id):

    if not authenticated(session):
        abort(401)

    seguimientos= Seguimiento.query.filter_by(denuncia=denuncia_id)
    denuncia(denuncia_id)

    return render_template("seguimiento/index.html",seguimientos=seguimientos,denuncia_id=denuncia_id)

def new():


    if not authenticated(session):
        abort(401)
    users = User.query.all()
    return render_template("Seguimiento/new.html", users=users)

def create():
    """
        El metodo ,si esta autenticado, creara una nueva denuncia
    """

    if not authenticated(session):
        abort(401)

    new_seguimiento = Seguimiento(**request.form)
    new_seguimiento.denuncia= denuncia
    try:
        Seguimiento.save(new_seguimiento)
    except:
        flash("Fallo al cargar el seguimiento", "error")
        return redirect(request.referrer)

    seguimientos= Seguimiento.query.filter_by(denuncia=denuncia)

    return render_template("seguimiento/index.html",seguimientos=seguimientos,denuncia_id=denuncia)


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
