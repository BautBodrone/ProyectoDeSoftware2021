from flask import redirect, render_template, request, url_for

from app.models.issue import Issue
#from app.models.rol import Rol

'Mostrara todos las consultas en pantalla'
# Public resources
def index():
    
    issues = Issue.query.all()

    return render_template("issue/index.html", issues=issues)

'El metodo hara una pagina para que crees una nueva consulta'
def new():
    return render_template("issue/new.html")

'El metodo creara una nueva consulta'
def create():
    
    new_issue = Issue(**request.form)
    Issue.save(new_issue)

    return redirect(url_for("issue_index"))
