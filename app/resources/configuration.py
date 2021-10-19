from flask import Flask, render_template, request, session, redirect, url_for

from app.models.configuration import Configuration
from app.helpers.auth import authenticated

def index():
    """
        El metodo mostrara una pagina para cambiar las configuraciones de la misma
    """

    configurations = Configuration.query.first()
    
    return render_template("config/index.html", configurations=configurations)

def save():
    """
        El metodo, si estas autenticado, actualizara las configuraciones del sistema
    """

    if not authenticated(session):
        abort(401)
    
    configurations = Configuration.query.first()
    configurations.update(request.form)
    return redirect(url_for("home"))