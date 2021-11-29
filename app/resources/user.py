from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.user import User
from app.helpers.auth import authenticated
from app.helpers.user_helper import has_permit
from app.helpers import configurator

from app.helpers.forms import UserForm, UserUpdateForm

from sqlalchemy import exc

# Protected resources
def index():
    """
        El metodo mostrara todos los usuarios en una tabla
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("user_index"):
        flash("No cuenta con los permisos necesarios")
        return render_template("home.html")

    page = request.args.get('page',1, type=int)
    page_config = configurator.settings().get_rows_per_page()
    users = User.query.paginate(page=page,per_page=page_config)


    return render_template("user/index.html", users=users)


def new():
    """
        El metodo ,si esta autenticado,saltara a una nueva pagina para crear un usuario
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("user_new"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    form = UserForm()

    return render_template("user/new.html", form=form)


def create():
    """
        El metodo ,si esta autenticado, creara un nuevo usuario
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("user_new"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)
    
    form = UserForm()
    if not form.validate_on_submit():
        flash(form.errors)
        return render_template("user/new.html", form=form)
    
    try:
        data= dict(form.data)
        del data["csrf_token"]
        new_user = User(**data)
        User.save(new_user)
    
        return redirect(url_for("user_index"))
    except exc.IntegrityError:
        flash("Usuario con ese nombre o email ya existe", "danger")
        return redirect(request.referrer)

def delete():
    """
        El metodo ,si esta autenticado, eliminara al usuario seleccionado
    """

    if not authenticated(session):
        abort(401)

    if not has_permit("user_delete"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    user = User.search_user(request.form["user_id"])
    user.delete()
    flash("Se elimino con exito")

    return redirect(url_for('user_index'))

def edit(user_id):
    """
        El metodo ,si esta autenticado, saltara a una nueva pagina para editar un usuario
    """
    if not authenticated(session):
        abort(401)

    if not has_permit("user_edit"):
        flash("No cuenta con los permisos necesarios")
        return redirect(request.referrer)

    user = User.search_user(user_id)
    form = UserUpdateForm()     
    
    return render_template("user/edit.html", form=form, user=user)

def edit_finish():
    """
        El metodo , si esta autentiticado, podra cambiar los datos de un usuario
    """

    if not authenticated(session):
        abort(401)

    form = UserForm()  
    data= dict(form.data)
    del data["csrf_token"]
    data = request.form
    user = User.search_user(data["id"])

    try:
        user.edit(data)
    except:
        flash("Usuario con ese nombre o email ya existe", "error")
        return redirect(request.referrer)

    return redirect(url_for("user_index"))

def add_rols():
    """
        El metodo ,si esta autenticado, añadira el nuevo rol al usuario seleccionado 
    """
    
    if not authenticated(session):
        abort(401)

    user_id = request.args["user_id"]
    roles = request.form.getlist("roles[]")
    for rol in roles:
        User.rols.add(user_id, rol)

    flash("Insercion exitosa", "success")

    return redirect(request.referrer)

def filtro():
    """
        El metodo hara un filtro de los usuarios dependiendo de los datos ingresados 
    """
    page_config = configurator.settings().get_rows_per_page()
    page = request.args.get('page',1, type=int)
    data = request.form
    activo = data["activo"]
    first_name = data["first_name"]
    if (activo != "" and first_name!= ""):
      users=User.query.filter_by(activo=activo,first_name=first_name).paginate(page=page,per_page=page_config)
    else:
        if (activo == "" and first_name != ""):
            users=User.query.filter_by(first_name=first_name).paginate(page=page,per_page=page_config)
        else:
            if(activo !="" and first_name==""):
                users=User.query.filter_by(activo=activo).paginate(page=page,per_page=page_config)
            else:
                users=User.query.paginate(page=page,per_page=page_config)
    return render_template("user/index.html", users=users )
