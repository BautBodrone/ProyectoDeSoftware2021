from flask import redirect, render_template, request, url_for, session, abort, flash

from app.models.puntos import Puntos
from app.helpers.auth import authenticated
from app.db import db

pagConf=4
# Public resources
def index():
    if not authenticated(session):
        abort(401)
    page = request.args.get('page',1, type=int)
    puntos = Puntos.query.paginate(page=page,per_page=pagConf)
    return render_template("puntosDeEncuentro/index.html", puntos=puntos)


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

def filtro():
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    nombre = data["nombre"]
    if (estado != "" and nombre!= ""):
      puntos=Puntos.query.filter_by(estado=estado,nombre=nombre).paginate(page=page,per_page=pagConf)
    else:
        if (estado == "" and nombre != ""):
            puntos=Puntos.query.filter_by(nombre=nombre).paginate(page=page,per_page=pagConf)
        else:
            if(estado !="" and nombre==""):
                puntos=Puntos.query.filter_by(estado=estado).paginate(page=page,per_page=pagConf)
            else:
                 puntos = Puntos.query.paginate(page=page,per_page=pagConf)
    return render_template("puntosDeEncuentro/index.html", puntos=puntos)



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