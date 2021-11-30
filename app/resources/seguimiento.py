from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.seguimiento import Seguimiento
from app.helpers.auth import authenticated
from app.db import db
from app.models.user import User
from app.models.denuncia import Denuncia

def index(denuncia_id):

    if not authenticated(session):
        abort(401)

    seguimientos= Seguimiento.query.filter_by(denuncia_id=denuncia_id)
    # denuncia(denuncia_id)

    return render_template("seguimiento/index.html",seguimientos=seguimientos,denuncia=denuncia_id)

def new(denuncia_id):

    if not authenticated(session):
        abort(401)
    users = User.query.all()
    return render_template("Seguimiento/new.html", users=users, denuncia=denuncia_id)

def create(denuncia_id):
    """
        El metodo ,si esta autenticado, creara un nuevo seguimiento
    """

    if not authenticated(session):
        abort(401)

    new_seguimiento = Seguimiento(**request.form)
    new_seguimiento.denuncia_id= denuncia_id
    try:
        Seguimiento.save(new_seguimiento)
    except:
        flash("Fallo al cargar el seguimiento", "error")
        return redirect(request.referrer)

    seguimientos= Seguimiento.query.filter_by(denuncia=denuncia_id)

    return render_template("seguimiento/index.html",seguimientos=seguimientos,denuncia_id=denuncia_id)


def delete():
    """
        El metodo ,si esta autenticado, eliminara el seguimiento
    """

    if not authenticated(session):
        abort(401)

    seguimiento = Seguimiento.search_denuncia(request.form["seguimiento_id"])
    seguimiento.delete()
    flash("Se elimino con exito")

    return redirect(url_for('seguimiento_index'))
