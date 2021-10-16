from os import path, environ

from flask import Flask, render_template, g, Blueprint, abort
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_session import Session
from flask_sqlalchemy import _SessionSignalEvents
from app.helpers.auth import authenticated

from config import config
from app import db
from app.db import db
from app.resources import issue, user, auth, puntos
from app.models.puntos import Puntos
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers import auth as helper_auth


def create_app(environment="production"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

    #Rutas de Puntos de encuentro
    app.add_url_rule("/puntosDeEncuentros", "puntos_index", puntos.index)
    app.add_url_rule("/puntos", "puntos_create", puntos.create, methods=["POST"])
    app.add_url_rule("/puntosDeEncuentros/nuevo", "puntos_new", puntos.new)
    #Editar punto de encuentro
    app.add_url_rule("/puntosDeEncuentro/edit/<id>", "puntos_edit", puntos.edit)
    app.add_url_rule("/puntosDeEncuentro/update","puntos_update",puntos.update, methods=["POST"])
    #Eliminar punto de encuentro
    @app.route('/puntosDeEncuentro/delete/<id>')
    def delete(id):
        puntoEliminar = Puntos.query.filter_by(id=int(id)).first()
        Puntos.delete(puntoEliminar)
        return redirect(url_for('puntos_index'))
    #Filtrar puntos de encuentro 
    app.add_url_rule("/puntosDeEncuentros", "puntos_filtro", puntos.filtro, methods=["POST"])

    @app.route('/api/data')
    def data():
        return {'data': [puntos.to_dict() for puntos in Puntos.query]}


    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
