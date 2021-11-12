from os import path, environ

from flask import Flask, render_template, g, Blueprint, abort, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_session import Session
from flask_sqlalchemy import _SessionSignalEvents
from app.helpers.auth import authenticated

from config import config
from app import db
from app.resources import user, auth, rol , configuration, punto, zona, home, permiso
from app.resources.api.zona import zonas_api
from app.resources.api.denuncias import denuncias_api
from app.helpers import handler, user_helper, configurator

from app.models.punto import Punto

from app.helpers import handler, user_helper
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
    
    # home
    app.add_url_rule("/", "home", home.index)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    #Rutas de Zonas
    app.add_url_rule("/zonas", "zona_index", zona.index)
    app.add_url_rule("/zonas/nuevo", "zona_new", zona.new)
    app.add_url_rule("/zonas", "zona_create", zona.create, methods=["POST"])
    app.add_url_rule("/zonas/delete","zona_delete", zona.delete, methods=["POST"])
    app.add_url_rule("/zonas/edit/<id>", "zona_edit", zona.edit)
    app.add_url_rule("/zonas/update","zona_update", zona.update, methods=["POST"])
    app.add_url_rule("/zonas/filtro","zona_filtro", zona.filtro, methods=["POST"] )

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

    # Ruta de permisos
    app.add_url_rule("/permisos","permiso_index", permiso.index)

    # Rutas de la configuracion
    app.add_url_rule("/configuracion", "configuration_edit", configuration.edit)
    app.add_url_rule("/configuracion", "configuration_update", configuration.save, methods=["POST"])

    #Rutas de Puntos de encuentro
    app.add_url_rule("/puntos", "punto_index", punto.index)
    app.add_url_rule("/puntos", "punto_create", punto.create, methods=["POST"])
    app.add_url_rule("/puntos/nuevo", "punto_new", punto.new )
    app.add_url_rule("/puntos/filtro","punto_filtro",punto.filtro, methods=["POST"] )

    #Editar punto de encuentro
    app.add_url_rule("/puntos/edit/<id>", "punto_edit", punto.edit)
    app.add_url_rule("/puntos/update","punto_update",punto.update, methods=["POST"])  
    app.add_url_rule("/puntos/delete/<id>", "punto_delete", punto.delete, methods=["POST"])

    # Rutas del api zonas
    # app.add_url_rule("/zonas-inundables", "api_zona_index", zonas_api.index)
    # app.add_url_rule("/zonas-inundables/:<id>", "/", zonas_api.get_id)

    # Rutas del api denuncias
    #app.add_url_rule("/denuncias", "/", api.denuncias.index, methods=["POST"])
    

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    
    api.register_blueprint(zonas_api)
    api.register_blueprint(denuncias_api)
    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(400, handler.bad_request)
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.server_error)
    
    # Retornar la instancia de app configurada
    return app
