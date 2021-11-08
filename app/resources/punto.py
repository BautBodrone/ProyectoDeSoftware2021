from flask import redirect, render_template, request, url_for, session, abort, flash

from app.models.punto import Punto
from app.helpers.auth import authenticated
from app.db import db

pagConf=4
# Public resources
def index():
    if not authenticated(session):
        abort(401)

    return render_template("punto/index.html")

def new():
    """
        El metodo , si esta autenticado, mostrara una pagina para crear un nuevo punto de encuentro
    """

    if not authenticated(session):
        abort(401)
    return render_template("punto/new.html")

def create():
    """
        El metodo ,si esta autenticado, creara un nuevo punto de encuentro
    """

    if not authenticated(session):
        abort(401)
    puntoNuevo = Punto(**request.form)
    try:
        Punto.save(puntoNuevo)
    except:
        flash("error")
        return redirect(request.referrer)

    flash("Se creo con exito", "success")
    return redirect(url_for("punto_index"))

def delete(id):
    """
        El metodo ,si esta autenticado, borrara un punto de encuentro
    """

    if not authenticated(session):
        abort(401)

    puntoEliminar = Punto.query.filter_by(id=int(id)).first()
    Punto.delete(puntoEliminar)
    flash("Se elimino con exito", "success") 
    return redirect(url_for('punto_index'))

def edit(id):
    """
        El metodo ,si esta autenticado, editara un punto de encuentro en una nueva pagina
    """

    if not authenticated(session):
        abort(401)
    punto = Punto.query.filter_by(id=int(id)).first()
    return render_template("punto/edit.html", punto=punto)

def update():
    """
        El metodo ,si esta autenticado, editara el punto de encuentro
    """

    data = request.form
    punto = Punto.search_punto(data["id"])
    try:
        punto.update(data)
    except:
        flash("error")
        return redirect(request.referrer)
    flash("Se edito con exito", "success")
    return redirect(url_for("puntos_index"))

def data():
    """
        El metodo hara un filtro de los puntos de encuentro dependiendo de los datos ingresados
    """

    query = Punto.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Punto.nombre.like(f'%{search}%'),
            Punto.estado.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [Punto.to_dict() for puntos in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Punto.query.count(),
        'draw': request.args.get('draw', type=int),
    }