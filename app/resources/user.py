from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.user import User
from app.helpers.auth import authenticated

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.query.all()

    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    new_user = User(**request.form)
    User.save(new_user)
    
    return redirect(url_for("user_index"))

def delete():
    if not authenticated(session):
        abort(401)

    user = User.search_user(request.form["user_id"])
    user.delete()
    flash("Se elimino con exito")

    return redirect(url_for('user_index'))
