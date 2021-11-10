from os import path, environ

from flask import Flask, render_template, g, Blueprint, abort, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_session import Session
from flask_sqlalchemy import _SessionSignalEvents
from app.helpers.auth import authenticated
from app.models import denuncia

from config import config

from app.resources import issue, user, auth, rol, configuration, puntos, denuncia
from app.db import db
from app.models.puntos import Puntos
from app.models.user import User
from app.resources.api.issue import issue_api
from app.helpers import handler, user_helper, configurator
from app.helpers import auth as helper_auth
from app.models.configuration import Configuration


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
    app.jinja_env.globals.update(get_private_bg_color=configurator.private_bg_color)
    app.jinja_env.globals.update(get_private_letters_color=configurator.private_letters_color)
    app.jinja_env.globals.update(get_private_accent_color=configurator.private_accent_color)
    app.jinja_env.globals.update(rows_per_page=configurator.rows_per_page)

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
    app.add_url_rule("/usuarios/filtro","user_filtro",user.filtro, methods=["POST"] )

    # Ruta de Roles
    app.add_url_rule("/roles", "rol_index", rol.index)

    # Rutas de configuracion
    app.add_url_rule("/configuracion", "configuration_index", configuration.index)
    app.add_url_rule("/configuracion", "configuration_update", configuration.save, methods=["POST"])

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


   #  Rutas de Denuncias
    app.add_url_rule("/denuncias", "denuncia_index", denuncia.index)
    app.add_url_rule("/denuncias", "denuncia_create", denuncia.create, methods=["POST"])
    app.add_url_rule("/denuncias/nuevo", "denuncia_new", denuncia.new)
    app.add_url_rule("/denuncias/delete", "denuncia_delete", denuncia.delete, methods=["POST"])
    app.add_url_rule("/denuncias/edit/<denuncia_id>","denuncia_edit",denuncia.edit)
    app.add_url_rule("/denuncias/edit","denuncia_edit_finish",denuncia.edit_finish, methods=["POST"])
    app.add_url_rule("/denuncias/filtro","denuncia_filtro",denuncia.filtro, methods=["POST"] )

    #DATA TABLE
    @app.route('/api/data')
    def data():
        puntos = Puntos.query
        # search filter
        search = request.args.get('search[value]')
        if search:
            puntos = puntos.filter(db.or_(
                Puntos.nombre.like(f'%{search}%'),
                Puntos.estado.like(f'{search}%'),
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
        'recordsTotal': Puntos.query.count(),
        'draw': request.args.get('draw', type=int),
    }

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        configurations = Configuration.query.first()
        app.jinja_env.globals.update(configurations=configurations)
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
