from flask.templating import render_template
from flask import flash, redirect, render_template, request, url_for, session, abort

from app.helpers.auth import authenticated
from app.helpers.user_helper import has_permit
from app.models.recorrido import Recorrido
from app.helpers import configurator

def index():
    """
        Busca de confi la cantidad de paginas y cantidad de elementos que debe mostrar
        Luego metodo mostrara todos los recorridos en una tabla
    """
    page = request.args.get('page',1, type=int)
    page_config = configurator.settings().get_rows_per_page()
    recorridos = Recorrido.query.paginate(page=page,per_page=page_config)

    return render_template("recorrido/index.html", recorridos=recorridos)

def new():
    """
        El metodo ,si esta autenticado,saltara a una nueva pagina para crear un recorrido
    """
    recorridos = Recorrido.query.all()
    return render_template("recorrido/new.html", recorridos=recorridos)

def create():
    """
        El metodo ,si esta autenticado, creara un nuevo recorrido
    """
    req = request.form
    new_recorrido = Recorrido(nombre=req["nombre"],estado=req["estado"],
    descripcion=req["descripcion"],coordenadas=req.getlist("coordenadas"))

    try:
        Recorrido.save(new_recorrido)
    except:
        flash("Ya existe otro recorrido con ese nombre", "error")
        return redirect(request.referrer)

    return redirect(url_for("recorrido_index"))

def edit(id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar un recorrido
        Se busca el objeto por id para podes poner los placeholders con sus
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("recorrido_edit"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    recorrido = Recorrido.query.filter_by(id=int(id)).first()
    return render_template("recorrido/edit.html", recorrido=recorrido)


def update():
    """
        El metodo , si esta autentiticado, podra cambiar los datos de un recorrido
    """
    
    data = request.form
    recorrido = Recorrido.search_id(data["id"])
    try:
        recorrido.update(data)
    except:
        flash("Ya existe otro recorrido con ese nombre")
        return redirect(request.referrer)
    flash("Se edito con exito", "success")
    return redirect(url_for("recorrido_index"))

def delete():
    """
        El metodo ,si esta autenticado, eliminara al recorrido seleccionado
        por interfaz
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("recorrido_delete"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    recorrido = Recorrido.search_id(request.form["recorrido_id"])
    recorrido.delete()
    flash("Se elimino con exito")

    return redirect(url_for('recorrido_index'))

def filtro():
    """
        El metodo hara un filtro de los recorridos dependiendo de los datos ingresados 
    """
    page_config = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    nombre = data["nombre"]
    if (estado != "" and nombre!= ""):
      recorridos=Recorrido.query.filter_by(estado=estado,nombre=nombre).paginate(page=page,per_page=page_config)
    else:
        if (estado == "" and nombre != ""):
            recorridos=Recorrido.query.filter_by(nombre=nombre).paginate(page=page,per_page=page_config)
        else:
            if(estado !="" and nombre==""):
                recorridos=Recorrido.query.filter_by(estado=estado).paginate(page=page,per_page=page_config)
            else:
                recorridos=Recorrido.query.paginate(page=page,per_page=page_confif)
    return render_template("recorrido/index.html", recorridos=recorridos )
