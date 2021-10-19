from flask import redirect, render_template, request, url_for

from app.models.issue import Issue

# Public resources
def index():
    """
        Mostrara todos las consultas en pantalla    
    """
    
    issues = Issue.query.all()

    return render_template("issue/index.html", issues=issues)

def new():
    """
        El metodo hara una pagina para que crees una nueva consulta
    """

    return render_template("issue/new.html")

def create():
    """
        El metodo creara una nueva consulta
    """

    new_issue = Issue(**request.form)
    Issue.save(new_issue)

    return redirect(url_for("issue_index"))
