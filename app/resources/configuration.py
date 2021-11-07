from flask import Flask, render_template, request, session, redirect, url_for, abort

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
    
    Configuration.get_config().update(request.form)

    return redirect(url_for("home"))