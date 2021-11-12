from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models import coordenada
from app.models.coordenada import Coordenada
from app.helpers.user_helper import has_permit
from app.models.punto import Punto
from app.helpers.auth import authenticated
from app.db import db
from app.helpers import configurator


# Public resources
def index():
    """
        El metodo mostrara todos los puntos en una tabla
    """

    if not authenticated(session):
        abort(401)

    page = request.args.get('page',1, type=int)
    page_config = configurator.settings().get_rows_per_page()
    puntos = Punto.query.paginate(page=page,per_page=page_config)

    return render_template("punto/index.html", puntos=puntos)


def new():
    if not authenticated(session):
        abort(401)

    if not has_permit("punto_index"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    return render_template("punto/new.html")


def create():
    if not authenticated(session):
        abort(401)
    
    puntoNuevo = Punto(**request.form)

    if not has_permit("punto_new"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    try:
        Punto.save(puntoNuevo)
        flash("Nuevo punto creado")
    except:
        flash("error")
        return redirect(request.referrer)

    return redirect(url_for("punto_index"))


def delete(id):
    if not authenticated(session):
        abort(401)

    if not has_permit("punto_delete"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    puntoEliminar = Punto.query.filter_by(id=int(id)).first()
    Punto.delete(puntoEliminar)
    flash("Se elimino con exito", "success") 
    return redirect(url_for('punto_index'))

def edit(id):
    if not authenticated(session):
        abort(401)

    if not has_permit("punto_edit"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    punto = Punto.query.filter_by(id=int(id)).first()
    return render_template("punto/edit.html", punto=punto)

def new():
    """
        El metodo , si esta autenticado, mostrara una pagina para crear un nuevo punto de encuentro
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("punto_index"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    coordenadas = Coordenada.query.all()

    return render_template("punto/new.html", coordenadas=coordenadas)

def update():
    data = request.form
    punto = Punto.search_punto(data["id"])
    try:
        punto.update(data)
    except:
        flash("error")
        return redirect(request.referrer)
    flash("Se edito con exito", "success")
    return redirect(url_for("punto_index"))

def filtro():
    """
        El metodo hara un filtro de los puntos dependiendo de los datos ingresados 
    """
    page_config = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    nombre = data["nombre"]
    if (estado != "" and nombre!= ""):
      puntos=Punto.query.filter_by(estado=estado,nombre=nombre).paginate(page=page,per_page=page_config)
    else:
        if (estado == "" and nombre != ""):
            puntos=Punto.query.filter_by(nombre=nombre).paginate(page=page,per_page=page_config)
        else:
            if(estado !="" and nombre==""):
                puntos=Punto.query.filter_by(estado=estado).paginate(page=page,per_page=page_config)
            else:
                puntos=Punto.query.paginate(page=page,per_page=page_config)
    return render_template("punto/index.html", puntos=puntos, estado=estado, nombre=nombre )
