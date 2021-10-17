from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.user import User
from app.helpers.auth import authenticated

from app.models.user_rol import User_rol

# Protected resources
'El metodo mostrara todos los usuarios en una tabla'
def index():
    if not authenticated(session):
        abort(401)

    users = User.query.all()

    return render_template("user/index.html", users=users)

'El metodo ,si esta autenticado,saltara a una nueva pagina para crear un usuario '
def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

'El metodo ,si esta autenticado, creara un nuevo usuario'
def create():
    if not authenticated(session):
        abort(401)

    new_user = User(**request.form)
    try:
        User.save(new_user)
    except:
        flash("Usuario con ese nombre o email ya existe", "error")
        return redirect(request.referrer)
    
    return redirect(url_for("user_index"))

'El metodo ,si esta autenticado, eliminara al usuario seleccionado'
def delete():
    if not authenticated(session):
        abort(401)

    user = User.search_user(request.form["user_id"])
    user.delete()
    flash("Se elimino con exito")

    return redirect(url_for('user_index'))

'El metodo ,si esta autenticado, saltara a una nueva pagina para editar un usuario'
def edit(user_id):
    if not authenticated(session):
        abort(401)

    user = User.search_user(user_id)
    
    return render_template("user/edit.html", user=user)

'El metodo , si esta autentiticado, podra cambiar los datos de un usuario'
def edit_finish():
    if not authenticated(session):
        abort(401)

    data = request.form
    user = User.search_user(data["id"])

    try:
        user.edit(data)
    except:
        flash("Usuario con ese nombre o email ya existe", "error")
        return redirect(request.referrer)

    return redirect(url_for("user_index"))

'El metodo ,si esta autenticado, añadira el nuevo rol al usuario seleccionado'
def add_rols():
    if not authenticated(session):
        abort(401)

    user_id = request.args["user_id"]
    roles = request.form.getlist("roles[]")
    for rol in roles:
        User_rol.add(user_id, rol)

    flash("Insercion exitosa", "success")

    return redirect(request.referrer)

'El metodo hara un filtro de los usuarios dependiendo de los datos ingresados '
def filtro():
    data = request.form
    activo = data["activo"]
    first_name = data["first_name"]
    if (activo != "" and first_name!= ""):
      users=User.query.filter_by(activo=activo,first_name=first_name)
    else:
        if (activo == "" and first_name != ""):
            users=User.query.filter_by(first_name=first_name)
        else:
            if(activo !="" and first_name==""):
                users=User.query.filter_by(activo=activo)
            else:
                 users=User.query.all()
    return render_template("user/index.html", users=users )
