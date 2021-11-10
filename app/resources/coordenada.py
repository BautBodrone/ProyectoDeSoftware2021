from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.coordenada import Coordenada
from app.helpers.auth import authenticated
from app.helpers.user_helper import has_permit

def index():

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_index"):
    #     flash("No cuenta con los permisso necesarios")
    #     return redirect(request.referrer)

    coordenadas = Coordenada.query.all()

    return render_template("coordenada/index.html", coordenadas=coordenadas)
    
def new():
    """
        El metodo ,si esta autenticado,saltara a una nueva pagina para crear una coordenada
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_new"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    return render_template("coordenada/new.html")

def new_punto():
    """
        El metodo ,si esta autenticado,saltara a una nueva pagina para crear una coordenada
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_new"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    return render_template("coordenada/new_punto.html")

def create():
    """
        El metodo ,si esta autenticado, creara una nueva coordenada
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_create"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)
    
    new_coord = Coordenada(**request.form)
    
    try:
        Coordenada.save(new_coord)
    except:
        flash("Coordenada con esa longitud y latitud ya existe", "error")
        return redirect(request.referrer)
    
    return redirect(url_for("coordenada_index"))

def create_punto():
    """
        El metodo ,si esta autenticado, creara una nueva coordenada
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_create"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)
    
    new_coord = Coordenada(**request.form)
    try:
        Coordenada.save(new_coord)
    except:
        flash("Coordenada con esa longitud y latitud ya existe", "error")
        return redirect(request.referrer)
    
    return redirect(url_for("punto_nuevo"))

def delete():
    """
        El metodo ,si esta autenticado, eliminara la coordenada seleccionado
    """

    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_delete"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    coordenada = Coordenada.search_coordenada(request.form["coordenada_id"])
    coordenada.delete()
    flash("Se elimino con exito")

    return redirect(url_for('user_index'))

def edit(coordenada_id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar un coordenada
    """
    if not authenticated(session):
        abort(401)

    # if not has_permit("coordenada_edit"):
    #     flash("No cuenta con los permisos necesarios")
    #     return redirect(request.referrer)

    coordenada = Coordenada.search_coordenada(coordenada_id)
    
    return render_template("coordenada/edit.html", coordenada=coordenada)

def edit_finish():
    """
        El metodo , si esta autentiticado, podra cambiar los datos de un coordenada
    """

    if not authenticated(session):
        abort(401)

    data = request.form
    coordenada = Coordenada.search_coordenada(data["id"])

    try:
        coordenada.edit(data)
    except:
        flash("Coordenada con esa longitud y latitud ya existe", "error")
        return redirect(request.referrer)

    return redirect(url_for("coordenada_index"))
