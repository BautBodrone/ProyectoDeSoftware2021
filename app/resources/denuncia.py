from flask import flash, redirect, render_template, request, url_for, session, abort
from app.models import denuncia

from app.models.denuncia import Denuncia
from app.helpers.auth import authenticated
from app.db import db
from sqlalchemy import and_
from app.models.user import User
from app.helpers import configurator
from app.helpers.forms import DenunciaForm, DenunciaEditForm
from app.helpers.user_helper import has_permit

from sqlalchemy import exc

# Protected resources
def index():
    """
        El metodo mostrara todos las denuncias en una tabla
    """
    
    pagConf = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    denuncias = Denuncia.query.paginate(page=page,per_page=pagConf)
    
    return render_template("denuncia/index.html", denuncias=denuncias)

def show(id):
    """
        muestra la info de la denuncia   
    """
    denuncia = Denuncia.query.filter_by(id=int(id)).first()
    return render_template("denuncia/show.html",denuncia=denuncia)

def show_map(id):
    """
        muestra el mapa dibujando la denuncia del id    
    """
    denuncia = Denuncia.query.filter_by(id=int(id)).first()
    return render_template("denuncia/map.html",denuncia=denuncia)

def new():


    if not has_permit("denuncia_new"):
        flash("No cuenta con los permisos necesarios","danger")
        return redirect(request.referrer)

    form = DenunciaForm()
    form.asignadoA.choices = [(g.id,g.username) for g in User.query.order_by('username')]
    
    return render_template("denuncia/new.html", form=form)

def create():
    """
        El metodo ,si esta autenticado, creara una nueva denuncia
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("denuncia_new"):
        flash("No cuenta con los permisos necesarios","danger")
        return redirect(request.referrer)
    
    form = DenunciaForm()
    form.asignadoA.choices = [(g.id,g.username) for g in User.query.order_by('username')]
    
    data= dict(form.data)
    
    if not form.validate_on_submit():
        return render_template("denuncia/new.html", form=form)
    
    data= dict(form.data)
    del data["csrf_token"]
    
    try:
        denuncia = Denuncia(**data)
        Denuncia.save(denuncia)
        flash("Se creo con exito", "success")
        return redirect(url_for("denuncia_index"))
        
    except exc.IntegrityError:
        flash("Denuncia con ese titulo ya existe", "error")
        return redirect(request.referrer)

def delete():
    """
        El metodo ,si esta autenticado, eliminara la denuncia seleccionada
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("denuncia_delete"):
        flash("No cuenta con los permisos necesarios","danger")
        return redirect(request.referrer)

    denuncia = Denuncia.search_denuncia(request.form["denuncia_id"])
    denuncia.delete()
    flash("Se elimino con exito", "success")

    return redirect(url_for('denuncia_index'))

def edit(denuncia_id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar una denuncia
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("denuncia_edit"):
        flash("No cuenta con los permisos necesarios","danger")
        return redirect(request.referrer)

    denuncia = Denuncia.search_denuncia(denuncia_id)
    form = DenunciaEditForm()
    form.asignadoA.choices = [(g.id,g.username) for g in User.query.order_by('username')]
    
    return render_template("denuncia/edit.html", denuncia=denuncia,form=form)

def edit_finish():

    if not authenticated(session):
        abort(401)

    if not has_permit("denuncia_edit"):
        flash("No cuenta con los permisos necesarios","danger")
        return redirect(request.referrer)

    form = DenunciaEditForm()
    data= dict(form.data)
    del data["csrf_token"]
    form.asignadoA.choices = [(g.id,g.username) for g in User.query.order_by('username')]
    
    denuncia = Denuncia.query.filter_by(id=data["id"]).first()
    
    if not form.validate_on_submit():
        flash(form.errors)
        return render_template("denuncia/edit.html", denuncia=denuncia, form=form)
    try:
        denuncia.edit(data)
        flash("Se edito con exito", "success")
        return redirect(url_for("denuncia_index"))
    except exc.IntegrityError:
        flash("Denuncia con ese titulo o coordenadas ya existe", "error")
        return redirect(request.referrer)

def filtro():
    """
        El metodo hara un filtro de las denuncias dependiendo de los datos ingresados 
    """
    pagConf = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    titulo = data["titulo"]
    fechaC = data["fechaC"]
    fechaF = data["fechaF"]
    busqueda = "%{}%".format(titulo)
    
    if (estado != "" and titulo != ""):
      denuncias=Denuncia.query.filter(Denuncia.titulo.like(busqueda),Denuncia.estado.like(estado)).paginate(page=page,per_page=pagConf)
    else:
        if (estado == "" and titulo != ""):
            denuncias=Denuncia.query.filter(Denuncia.titulo.like(busqueda)).paginate(page=page,per_page=pagConf)
        else:
            if (estado != "" and titulo == ""):
                denuncias=Denuncia.query.filter_by(estado=estado).paginate(page=page,per_page=pagConf)
            else:
                 denuncias=Denuncia.query.paginate(page=page,per_page=pagConf)

    if (fechaC != "" and fechaF !="" ):
          denuncias=denuncias.query.filter(and_(Denuncia.fechaC >= fechaC , Denuncia.fechaC<= fechaF)).paginate(page=page,per_page=pagConf)
    else:
        if (fechaC != "" and fechaF =="" ):  
                denuncias=denuncias.query.filter(Denuncia.fechaC >= fechaC).paginate(page=page,per_page=pagConf)
        else:
            if (fechaC == "" and fechaF !="" ):  
                denuncias=denuncias.query.filter(Denuncia.fechaF <= fechaF).paginate(page=page,per_page=pagConf)
    return render_template("denuncia/index.html", denuncias=denuncias , titulo=titulo )

