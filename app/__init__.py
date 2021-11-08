from os import path, environ

from flask import Flask, render_template, g, Blueprint, abort, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_session import Session
from flask_sqlalchemy import _SessionSignalEvents
from app.helpers.auth import authenticated

from config import config
from app import db
from app.resources import user, auth, rol , configuration, puntos
from app.helpers import handler, user_helper, configurator
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
    app.jinja_env.globals.update(my_user=user_helper.user)
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(is_admin=user_helper.is_admin)
    app.jinja_env.globals.update(configurator=configurator.settings)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/delete", "user_delete", user.delete, methods=["POST"])
    app.add_url_rule("/usuarios/edit/<user_id>","user_edit",user.edit)
    app.add_url_rule("/usuarios/edit","user_edit_finish",user.edit_finish, methods=["POST"])
    app.add_url_rule("/usuarios/filtro","user_filtro",user.filtro, methods=["POST"] )

    # Ruta de Roles
    app.add_url_rule("/roles", "rol_index", rol.index)

    # Rutas de la configuracion
    app.add_url_rule("/configuracion", "configuration_edit", configuration.edit)
    app.add_url_rule("/configuracion", "configuration_update", configuration.save, methods=["POST"])

    #Rutas de Puntos de encuentro
    app.add_url_rule("/puntosDeEncuentros", "puntos_index", puntos.index)
    app.add_url_rule("/puntos", "puntos_create", puntos.create, methods=["POST"])
    app.add_url_rule("/puntosDeEncuentros/nuevo", "puntos_new", puntos.new)
    app.add_url_rule("/puntosDeEncuentro/filtro","puntos_filtro",puntos.filtro, methods=["POST"] )

    #Editar punto de encuentro
    app.add_url_rule("/puntosDeEncuentro/edit/<id>", "puntos_edit", puntos.edit)
    app.add_url_rule("/puntosDeEncuentro/update","puntos_update",puntos.update, methods=["POST"])
    app.add_url_rule("/puntosDeEncuentro/delete/<id>", "puntos_delete", puntos.delete, methods=["POST"])

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.server_error)

    # Retornar la instancia de app configurada
    return app
