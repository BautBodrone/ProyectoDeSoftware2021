from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated

from app.models.punto import Punto

def index():
    
    if not authenticated(session):
        abort(401)

    puntos = Punto.query.all()

    return render_template("punto/index.html", puntos=puntos)

def new():

    if not authenticated(session):
        abort(401)

    return render_template("punto/new.html")

def create():
    if not authenticated(session):
        abort(401)

    new_punto = Punto(**request.form)
    Punto.save(new_punto)
    
    return redirect(url_for("punto_index"))

def delete():

    if not authenticated(session):
        abort(401)

    punto = Punto.search_punto(request.form['punto_nombre'])
    punto.delete()
    flash("Se elimino con exito") 
    return redirect(url_for("/puntos"))