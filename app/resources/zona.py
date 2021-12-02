from flask.templating import render_template
from flask import flash, redirect, render_template, request, url_for, session, abort

from app.helpers.auth import authenticated
from app.helpers.user_helper import has_permit
from app.models.zona import Zona
from app.helpers import configurator
import csv
from app.helpers.forms import ZonaForm, ZonaUpdateForm

from sqlalchemy import exc

def index():
    """
        El metodo mostrara todos las zonas en una tabla
    """

    page = request.args.get('page',1, type=int)
    page_config = configurator.settings().get_rows_per_page()
    zonas = Zona.query.paginate(page=page,per_page=page_config)

    return render_template("zona/index.html", zonas=zonas)

def new():
    """
        El metodo ,si esta autenticado,saltara a una nueva pagina para crear una zona
    """
    
    form = ZonaForm()
    
    return render_template("zona/new.html", form=form)

def show(id):
    """
         muestra el id
    """
    zona = Zona.query.filter_by(id=int(id)).first()
    return render_template("zona/show.html",zona=zona)

def show_map(id):
    """
         muestra el mapa dibujando la zona del id
    """
    zona = Zona.query.filter_by(id=int(id)).first()
    return render_template("zona/map.html",zona=zona)

def save_csv():
    """
        Este metodo carga el archivo csv, seteando por defecto "despublicado", 
        formateando las coordenadas a csv sin caracteres especiales.
    """
    if request.files:
        uploaded_file = request.files['csv']
        if '.csv' in uploaded_file.filename:  
            if uploaded_file.filename != '':
                csv_file = csv.DictReader(uploaded_file.read().decode('utf-8').splitlines())
                for row in csv_file:
                    if 'name' in row and 'area' in row:               
                        row['area'] = row['area'].translate(str.maketrans('', '', '{[]!@#$}'))
                        newZona = Zona(nombre=row['name'],estado='despublicado',coordenadas=row['area'])
                        try:
                            Zona.upload(newZona)
                        except:
                            flash("error", "error")
                            return redirect(request.referrer)
                    else:
                        flash("El archivo no cumple con los requerimientos")
        else: 
            flash("El archivo debe ser un .csv")
    return redirect(url_for("zona_index"))    
    
def create():
    """
        El metodo ,si esta autenticado, creara una nueva zona
    """
    req = request.form
    new_zona = Zona(nombre=req["nombre"],estado=req["estado"],
    color=req["color"],coordenadas=req.getlist("coordenadas"))
    
    form = ZonaForm()
    if not form.validate_on_submit():
        flash(form.errors)
        return render_template("zona/new.html", form=form)

    try:
        
        data= dict(form.data)
        del data["csrf_token"]
        new_zona = Zona(**data)
        Zona.save(new_zona)
    except exc.IntegrityError:
        flash("Zona con ese nombre ya existe", "danger")
        return redirect(request.referrer)

    return redirect(url_for("zona_index"))

def edit(id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar una zona
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("zona_edit"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    form = ZonaUpdateForm()
    
    zona = Zona.query.filter_by(id=int(id)).first()
    return render_template("zona/edit.html", form=form,zona=zona)


def update():
    """
        El metodo , si esta autentiticado, podra cambiar los datos de una zona
    """
    # req = request.form
    # data = Zona(nombre=req["nombre"],estado=req["estado"],
    # color=req["color"],coordenadas=req.getlist("coordenadas"))
    # zona = Zona.search_id(req["id"])
    
    form = ZonaUpdateForm()
    data= dict(form.data)
    del data["csrf_token"]
    print("-----------------------------------")
    print(data)
    zona = Zona.search_id(data["id"])
    try:
        zona.update(data)
    except:
        flash("error")
        return redirect(request.referrer)
    flash("Se edito con exito", "success")
    return redirect(url_for("zona_index"))

def delete():
    """
        El metodo ,si esta autenticado, eliminara a la zona
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("zona_delete"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    zona = Zona.search_id(request.form["zona_id"])
    zona.delete()
    flash("Se elimino con exito")

    return redirect(url_for('zona_index'))

def filtro():
    """
        El metodo hara un filtro de los zonas dependiendo de los datos ingresados 
    """
    page_config = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    data = request.form
    estado = data["estado"]
    nombre = data["nombre"]
    busqueda = "%{}%".format(nombre)
    if (estado != "" and nombre != ""):
      zonas=Zona.query.filter(Zona.nombre.like(busqueda),Recorrido.estado.like(estado)).paginate(page=page,per_page=page_config)
    else:
        if (estado == "" and nombre != ""):
            zonas=Zona.query.filter(Zona.nombre.like(busqueda)).paginate(page=page,per_page=page_config)
        else:
            if(estado !="" and nombre==""):
                zonas=Zona.query.filter_by(estado=estado).paginate(page=page,per_page=page_config)
            else:
                zonas=Zona.query.paginate(page=page,per_page=page_config)
    return render_template("zona/index.html", zonas=zonas )
