from os import path, environ

from flask import Flask, render_template, g, Blueprint
from flask_session import Session

from config import config
from app import db
from app.resources import issue, user, auth, punto #, permiso, rol
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers import auth as helper_auth
import boom


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
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/delete", "user_delete", user.delete, methods=["POST"])

    # Ruta de Puntos
    app.add_url_rule("/puntos", "punto_index", punto.index)
    app.add_url_rule("/puntos", "punto_create", punto.create, methods=["POST"])
    app.add_url_rule("/puntos/nuevo", "punto_new", punto.new)
    app.add_url_rule("/puntos/delete","punto_delete",punto.delete, methods=["POST"])
    app.add_url_rule("/puntos/edit/<punto_coordenadas1>","punto_edit",punto.edit, methods=["POST"])
    app.add_url_rule("/puntos/edit","punto_edit_finish",punto.edit_finish, methods=["POST"])


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
