from flask import redirect, render_template, request, url_for, session, abort, flash

from app.models.puntos import Puntos
from app.helpers.auth import authenticated
from app.db import db

pagConf=4
# Public resources
def index():
    if not authenticated(session):
        abort(401)
    
    return render_template("puntosDeEncuentro/index.html")


def new():
    if not authenticated(session):
        abort(401)
    return render_template("puntosDeEncuentro/new.html")


def create():
    if not authenticated(session):
        abort(401)
    puntoNuevo = Puntos(**request.form)
    try:
        Puntos.save(puntoNuevo)
    except:
        flash("error")
        return redirect(request.referrer)

    flash("Se creo con exito", "success")
    return redirect(url_for("puntos_index"))


def delete(id):
        if not authenticated(session):
          abort(401)

        puntoEliminar = Puntos.query.filter_by(id=int(id)).first()
        Puntos.delete(puntoEliminar)
        flash("Se elimino con exito", "success") 
        return redirect(url_for('puntos_index'))

def edit(id):
    if not authenticated(session):
        abort(401)
    punto = Puntos.query.filter_by(id=int(id)).first()
    return render_template("puntosDeEncuentro/edit.html", punto=punto)

def update():
    data = request.form
    punto = Puntos.search_punto(data["id"])
    try:
        punto.update(data)
    except:
        flash("error")
        return redirect(request.referrer)
    flash("Se edito con exito", "success")
    return redirect(url_for("puntos_index"))

def data():
    query = Puntos.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Puntos.nombre.like(f'%{search}%'),
            Puntos.estado.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [Puntos.to_dict() for puntos in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Puntos.query.count(),
        'draw': request.args.get('draw', type=int),
    }