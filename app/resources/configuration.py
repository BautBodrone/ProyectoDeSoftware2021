from flask import render_template, request, session, redirect, url_for, abort, flash

from app.models.configuration import Configuration
from app.helpers.auth import authenticated

def edit():
    """
        El metodo mostrara una pagina para cambiar las configuraciones de la misma
    """
    if not authenticated(session):
        abort(401)

    configurations = Configuration.get_config()
    
    return render_template("config/edit.html", configurations=configurations)

def save():
    if not authenticated(session):
        abort(401)
    try:
        Configuration.get_config().update(request.form)
    except:
        flash("error al actualizar las configuraciones")
        return redirect(request.referrer)

    return redirect(url_for("home"))