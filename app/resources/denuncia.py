from flask import flash, redirect, render_template, request, url_for, session, abort
from app.models import denuncia

from app.models.denuncia import Denuncia
from app.helpers.auth import authenticated
from app.db import db
from sqlalchemy import and_
from app.models.user import User


pagConf=4

# Protected resources
def index():
    """
        El metodo mostrara todos las denuncias en una tabla
    """

    if not authenticated(session):
        abort(401)

    page = request.args.get('page',1, type=int)
    denuncias = Denuncia.query.paginate(page=page,per_page=pagConf)
    
    return render_template("denuncia/index.html", denuncias=denuncias)

def new():


    if not authenticated(session):
        abort(401)
    users = User.query.all()
    return render_template("denuncia/new.html", users=users)

def create():
    """
        El metodo ,si esta autenticado, creara una nueva denuncia
    """

    if not authenticated(session):
        abort(401)

    new_denuncia = Denuncia(**request.form)
    
    new_denuncia.print()
    try:
        Denuncia.save(new_denuncia)
    except:
        flash("Denuncia con ese titulo o coordenadas ya existe", "error")
        return redirect(request.referrer)
    
    return redirect(url_for("denuncia_index"))

def delete():
    """
        El metodo ,si esta autenticado, eliminara al usuario seleccionado
    """

    if not authenticated(session):
        abort(401)

    denuncia = Denuncia.search_denuncia(request.form["denuncia_id"])
    denuncia.delete()
    flash("Se elimino con exito")

    return redirect(url_for('denuncia_index'))

def edit(denuncia_id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar un usuario
    """
    if not authenticated(session):
        abort(401)

    denuncia = Denuncia.search_denuncia(denuncia_id)
    
    return render_template("denuncia/edit.html", denuncia=denuncia)

def edit_finish():

    if not authenticated(session):
        abort(401)

    data = request.form
    denuncia = Denuncia.search_denuncia(data["id"])

    try:
        denuncia.edit(data)
    except:
        flash("Denuncia con ese titulo o coordenadas ya existe", "error")
        return redirect(request.referrer)

    return redirect(url_for("denuncia_index"))

def filtro():
    """
        El metodo hara un filtro de los usuarios dependiendo de los datos ingresados 
    """
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    titulo = data["titulo"]
    fechaC = data["fechaC"]
    fechaF = data["fechaF"]
    
    if (estado != "" and titulo != ""):
      denuncias=Denuncia.query.filter_by(estado=estado,titulo=titulo).paginate(page=page,per_page=pagConf)
    else:
        if (estado == "" and titulo != ""):
            denuncias=Denuncia.query.filter_by(titulo=titulo).paginate(page=page,per_page=pagConf)
        else:
            if (estado != "" and titulo == ""):
                denuncias=Denuncia.query.filter_by(estado=estado).paginate(page=page,per_page=pagConf)
            else:
                 denuncias=Denuncia.query.paginate(page=page,per_page=pagConf)

    if (fechaC != "" and fechaF !="" ):
          denuncias=denuncias.query.filter(and_(Denuncia.fechaC >= fechaC , Denuncia.fechaF<= fechaF)).paginate(page=page,per_page=pagConf)
    else:
        if (fechaC != "" and fechaF =="" ):  
                denuncias=denuncias.query.filter(Denuncia.fechaC >= fechaC).paginate(page=page,per_page=pagConf)
        else:
            if (fechaC == "" and fechaF !="" ):  
                denuncias=denuncias.query.filter(Denuncia.fechaF <= fechaF).paginate(page=page,per_page=pagConf)
    return render_template("denuncia/index.html", denuncias=denuncias )

