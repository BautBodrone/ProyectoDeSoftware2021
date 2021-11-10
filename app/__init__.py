from os import path, environ

from flask import Flask, render_template, g, Blueprint, abort, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_session import Session
from flask_sqlalchemy import _SessionSignalEvents
from app.helpers.auth import authenticated

from config import config
from app import db

from app.resources import issue, user, auth, punto, rol , configuration


from app.resources import issue, user, auth, rol, configuration, punto, coordenada
from app.db import db
from app.models.punto import Punto
from app.resources.api.issue import issue_api
from app.helpers import handler, user_helper
from app.helpers import auth as helper_auth
from app.helpers import configurator


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

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/delete", "user_delete", user.delete, methods=["POST"])
    app.add_url_rule("/usuarios/edit/<user_id>","user_edit",user.edit)
    app.add_url_rule("/usuarios/edit","user_edit_finish",user.edit_finish, methods=["POST"])

 # Ruta de Roles
    app.add_url_rule("/roles", "rol_index", rol.index)

    # Rutas de Usuarios
    app.add_url_rule("/configuracion", "configuration_edit", configuration.edit)
    app.add_url_rule("/configuracion", "configuration_update", configuration.save, methods=["POST"])

    # Rutas de Coordenadas
    app.add_url_rule("/coordenadas/index", "coordenada_index", coordenada.index)
    app.add_url_rule("/coordenadas/nuevo", "coordenada_new", coordenada.new)
    app.add_url_rule("/coordenadas/nuevo/punto", "coordenada_new_punto", coordenada.new_punto)
    app.add_url_rule("/coordenadas", "coordenada_create", coordenada.create, methods=["POST"])
    app.add_url_rule("/coordenadas", "coordenada_create_punto", coordenada.create_punto, methods=["POST"])

    #Rutas de Puntos de encuentro
    app.add_url_rule("/puntos", "punto_index", punto.index)
    app.add_url_rule("/puntos", "punto_create", punto.create, methods=["POST"])
    app.add_url_rule("/puntos/nuevo", "punto_new", punto.new)
    app.add_url_rule("/puntos/edit/<id>", "punto_edit", punto.edit)
    app.add_url_rule("/puntos/update","punto_update",punto.update, methods=["POST"])

    #Eliminar punto de encuentro
    @app.route('/puntos/delete/<id>')
    def delete(id):
        puntoEliminar = Punto.query.filter_by(id=int(id)).first()
        Punto.delete(puntoEliminar)
        return redirect(url_for('punto_index'))

    #DATA TABLE
    @app.route('/api/data')
    def data():
        puntos = Punto.query
        # search filter
        search = request.args.get('search[value]')
        if search:
            puntos = puntos.filter(db.or_(
                Punto.nombre.like(f'%{search}%'),
                Punto.estado.like(f'{search}%'),
            ))
        total_filtered = puntos.count()
        # pagination
        start = request.args.get('start', type=int)
        length = request.args.get('length', type=int)
        puntos = puntos.offset(start).limit(length)

        # response
        return {
        'data': [p.to_dict() for p in puntos],
        'recordsFiltered': total_filtered,
        'recordsTotal': Punto.query.count(),
        'draw': request.args.get('draw', type=int),
    }
        

        

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
    app.register_error_handler(500, handler.server_error)

    # Retornar la instancia de app configurada
    return app
