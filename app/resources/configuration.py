from flask import Flask, render_template, request, session, redirect, url_for, abort

from app.models.configuration import Configuration
from app.helpers.auth import authenticated

def edit():
    """
        El metodo mostrara una pagina para cambiar las configuraciones de la misma
    """

    configurations = Configuration.query.first()
    
    return render_template("config/edit.html", configurations=configurations)

def save():
    """
        El metodo, si estas autenticado, actualizara las configuraciones del sistema
    """

    if not authenticated(session):
        abort(401)
    
    Configuration.query.first().update(request.form)

    return redirect(url_for("home"))