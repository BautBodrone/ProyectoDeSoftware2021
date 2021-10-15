from flask import Flask, render_template, request, redirect, url_for

from app.models.configuration import Configuration

def index():
    configurations = Configuration.query.first()
    print("index")
    return render_template("config/index.html", configurations=configurations)

def save():
    if not authenticated(session):
        abort(401)
    configurations = Configuration.query.first()
    configurations.update(**request.form)
    return redirect(url_for("configuration_index"))

def bg_color():
    return Configuration.bg_color()