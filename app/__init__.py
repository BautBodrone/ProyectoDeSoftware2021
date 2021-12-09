from os import path, environ,urandom

from flask import Flask, Blueprint
from flask_session import Session
from flask_cors import CORS

from config import config
from app import db
from app.models.user import User
from app.resources import user, auth, rol , configuration, punto, zona, home, permiso, denuncia, seguimiento, recorrido
from app.resources.api.zona import zonas_api
from app.resources.api.denuncia import denuncias_api
from app.resources.api.puntos   import puntos_api
from app.resources.api.recorrido import recorrido_api
from app.resources.api.configuration import configuration_api
from app.helpers import handler, user_helper, configurator
from app.helpers import auth as helper_auth

from oauthlib.oauth2 import WebApplicationClient
from flask_login import (LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    )

GOOGLE_CLIENT_ID ="121321804230-vh5t42njjsba08v7iif6k2ceai2k83qm.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

def create_app(environment="production"):

    # Configuración inicial de la app
    app = Flask(__name__)
    CORS(app)

    app.secret_key = environ.get("SECRET_KEY") or urandom(24)

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
    app.add_url_rule("/iniciar", "auth_loginG", auth.loginG)
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])
    app.add_url_rule("/login/callback", "auth_callback", auth.callback, methods=["GET"])

    #Rutas de Zonas
    app.add_url_rule("/zonas", "zona_index", zona.index)
    app.add_url_rule("/zonas/map/<id>", "zona_show_map", zona.show_map)
    app.add_url_rule("/zonas/nuevo", "zona_new", zona.new)
    app.add_url_rule("/zonas/show/<id>", "zona_show", zona.show)
    app.add_url_rule("/zonas/edit/<id>", "zona_edit", zona.edit)
    app.add_url_rule("/zonas", "zona_create", zona.create, methods=["POST"])
    app.add_url_rule("/zonas/delete","zona_delete", zona.delete, methods=["POST"])
    app.add_url_rule("/zonas/upload","zona_csv", zona.save_csv, methods=["POST"])
    app.add_url_rule("/zonas/update","zona_update", zona.update, methods=["POST"])
    app.add_url_rule("/zonas/filtro","zona_filtro", zona.filtro, methods=["POST"])

    #Rutas de Recorridos
    app.add_url_rule("/recorridos", "recorrido_index", recorrido.index)
    app.add_url_rule("/recorridos/map/<id>", "recorrido_show_map", recorrido.show_map)
    app.add_url_rule("/recorrido/show/<id>", "recorrido_show", recorrido.show)
    app.add_url_rule("/recorridos/nuevo", "recorrido_new", recorrido.new)
    app.add_url_rule("/recorridos", "recorrido_create", recorrido.create, methods=["POST"])
    app.add_url_rule("/recorridos/delete","recorrido_delete", recorrido.delete, methods=["POST"])
    app.add_url_rule("/recorridos/edit/<id>", "recorrido_edit", recorrido.edit)
    app.add_url_rule("/recorridos/update","recorrido_update", recorrido.update, methods=["POST"])
    app.add_url_rule("/recorridos/filtro","recorrido_filtro", recorrido.filtro, methods=["POST"] )

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
    app.add_url_rule("/zonas/show/<id>", "zona_show", zona.show)
    app.add_url_rule("/puntos/nuevo", "punto_new", punto.new )
    app.add_url_rule("/puntos/filtro","punto_filtro",punto.filtro, methods=["POST"] )

    #Editar punto de encuentro
    app.add_url_rule("/puntos/edit/<id>", "punto_edit", punto.edit)
    app.add_url_rule("/puntos/map/<id>", "punto_show_map", punto.show_map)
    app.add_url_rule("/puntos/show/<id>", "punto_show", punto.show)
    app.add_url_rule("/puntos/update","punto_update",punto.update, methods=["POST"])  
    app.add_url_rule("/puntos/delete/<id>", "punto_delete", punto.delete, methods=["POST"])

     #  Rutas de Denuncias
    app.add_url_rule("/denuncias", "denuncia_index", denuncia.index)
    app.add_url_rule("/denuncias/map/<id>", "denuncia_show_map", denuncia.show_map)
    app.add_url_rule("/denuncias/show/<id>", "denuncia_show", denuncia.show)
    app.add_url_rule("/denuncias", "denuncia_create", denuncia.create, methods=["POST"])
    app.add_url_rule("/denuncias/nuevo", "denuncia_new", denuncia.new)
    app.add_url_rule("/denuncias/delete", "denuncia_delete", denuncia.delete, methods=["POST"])
    app.add_url_rule("/denuncias/edit/<denuncia_id>","denuncia_edit",denuncia.edit)
    app.add_url_rule("/denuncias/edit","denuncia_edit_finish",denuncia.edit_finish, methods=["POST"])
    app.add_url_rule("/denuncias/filtro","denuncia_filtro",denuncia.filtro, methods=["POST"] )

    #Rutas de seguimientos
    app.add_url_rule("/seguimiento/<denuncia_id>","seguimiento_index",seguimiento.index)
    app.add_url_rule("/seguimiento/<denuncia_id>", "seguimiento_create", seguimiento.create, methods=["POST"])
    app.add_url_rule("/seguimiento/nuevo/<denuncia_id>", "seguimiento_new", seguimiento.new)
    app.add_url_rule("/seguimiento/delete", "seguimiento_delete", seguimiento.delete, methods=["POST"])

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    
    api.register_blueprint(configuration_api)
    api.register_blueprint(puntos_api)
    api.register_blueprint(recorrido_api)
    api.register_blueprint(zonas_api)
    api.register_blueprint(denuncias_api)
    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(400, handler.bad_request)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(500, handler.server_error)
    
    # Retornar la instancia de app configurada
    return app
