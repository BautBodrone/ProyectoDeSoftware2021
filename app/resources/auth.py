from flask import redirect, render_template, request, url_for, abort, session, flash

from app.models.user import User

def login():
    """
        El metodo mostrara una nueva pagina para poder iniciar sesion
    """

    return render_template("auth/login.html")

def authenticate():
    """
        El metodo autentica la sesion del usuario
    """

    params = request.form

    user = User.authenticate_user(params)

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    if not user.is_activo():
        flash("Usuario bloqueado.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))

def logout():
    """
        El metodo cerrara la sesion
    """
    
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("home"))
