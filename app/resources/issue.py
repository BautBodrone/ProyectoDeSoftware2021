from flask import redirect, render_template, request, url_for

from app.models.issue import Issue
#from app.models.rol import Rol

# Public resources
def index():
    
    issues = Issue.query.all()
    #rols = Rol.query.all()

    return render_template("issue/index.html", issues=issues)


def new():
    return render_template("issue/new.html")


def create():
    
    new_issue = Issue(**request.form)
    Issue.save(new_issue)

    return redirect(url_for("issue_index"))
