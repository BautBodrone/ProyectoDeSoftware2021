from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app.models.user import User


def index():
    users = User.query.all()
    return render_template("probando/index.html",users=users)


#def tienePermisos


def authenticate():
    params = request.form

    user = User.authenticate_user(params)

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
