from flask import flash, redirect, render_template, request, url_for, session, abort

from app.models.zona import Zona

def index():
    
    zonas = Zona.query.all()

    return render_template("zonas/index.html", zonas=zonas)