from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated
from app.models.punto import Punto
import bleach

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
    flash("Se creo con exito", "success") 
    return redirect(url_for("punto_index"))

def delete():

    if not authenticated(session):
        abort(401)

    punto = Punto.search_punto(request.form["punto_id"])
    punto.delete()
    flash("Se elimino con exito", "success") 
    return redirect(url_for("punto_index"))

def edit(punto_coordenadas1):
    if not authenticated(session):
        abort(401)

    punto = Punto.search_punto(punto_coordenadas1)

    return render_template("punto/edit.html", punto=punto)


def edit_finish():

    if not authenticated(session):
        abort(401)

    print("tst")
    data = request.form
    punto = Punto.search_punto(data["coordenadas1"])

    dictUser = {
        "nombre": bleach.clean(data["nombre"]),
        "direccion": bleach.clean(data["direccion"]),
        "coordenadas1": bleach.clean(data["coordenadas1"]),
        "estado": bleach.clean(data["estado"]),
        "telefono": bleach.clean(data["telefono"]),
        "email": bleach.clean(data["email"])
    }

    punto.edit(dictUser)

    flash("Se edito con exito", "success")

    return redirect(url_for("punto_index"))