from flask.templating import render_template
from flask import flash, redirect, render_template, request, url_for, session, abort

from app.helpers.auth import authenticated
from app.helpers.user_helper import has_permit
from app.models.zona import Zona
from app.models.coordenada import Coordenada

def index():

    zonas = Zona.query.all()

    return render_template("zona/index.html", zonas=zonas)

def new():
    coordenadas = Coordenada.query.all()
    return render_template("zona/new.html", coordenadas=coordenadas)

def create():
    req = request.form
    new_zona = Zona(nombre=req["nombre"],estado=req["estado"],
    color=req["color"],coordenadas=req.getlist("coordenadas"))

    try:
        Zona.save(new_zona)
        flash("Se creo con exito", "success") 
    except:
        flash("error", "error")
        return redirect(request.referrer)

    return redirect(url_for("zona_index"))

def delete():
    if not authenticated(session):
        abort(401)

    # if not has_permit("zona_delete"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    zona = Zona.search_id(request.form["zona_id"])
    zona.delete()
    flash("Se elimino con exito")

    return redirect(url_for('zona_index'))