from flask import redirect, render_template, request, url_for, session, abort, flash

from app.helpers.user_helper import has_permit
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
    """
        El metodo , si esta autenticado, mostrara una pagina para crear un nuevo punto de encuentro
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("punto_index"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    return render_template("puntosDeEncuentro/new.html")

def create():
    """
        El metodo ,si esta autenticado, creara un nuevo punto de encuentro
    """

    if not authenticated(session):
        abort(401)
    puntoNuevo = Puntos(**request.form)

    if not has_permit("punto_new"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    try:
        Puntos.save(puntoNuevo)
    except:
        flash("error")
        return redirect(request.referrer)

    flash("Se creo con exito", "success")
    return redirect(url_for("puntos_index"))

def delete(id):
    """
        El metodo ,si esta autenticado, borrara un punto de encuentro
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("punto_delete"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    puntoEliminar = Puntos.query.filter_by(id=int(id)).first()
    Puntos.delete(puntoEliminar)
    flash("Se elimino con exito", "success") 
    return redirect(url_for('puntos_index'))

def edit(id):
    """
        El metodo ,si esta autenticado, editara un punto de encuentro en una nueva pagina
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("punto_edit"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    punto = Puntos.query.filter_by(id=int(id)).first()
    return render_template("puntosDeEncuentro/edit.html", punto=punto)

def update():
    """
        El metodo ,si esta autenticado, editara el punto de encuentro
    """

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
    """
        El metodo hara un filtro de los puntos de encuentro dependiendo de los datos ingresados
    """

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