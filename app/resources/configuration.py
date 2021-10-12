from flask import Flask, render_template, request, url_for

from app.models.configuration import Configuration

def index():
    configurations = Configuration.query.first()
    
    return render_template("config/index.html", configurations=configurations)

def update():
    #to be implemented
    new_config = Configuration(**request.form)
    Configuration.update(new_config)

    return render_template("config/index.html")