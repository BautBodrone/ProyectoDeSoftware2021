from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.configuration import ConfigurationSchema
from app.models.configuration import Configuration
import app.helpers.handler as handler

configuration_api = Blueprint("configuration-publica", __name__, url_prefix="/configuration-publica")


@configuration_api.get("/")
def get():    
    try:
        conf = Configuration.query.first()
        atributos = ConfigurationSchema.dump(conf)
        return jsonify(atributos)
    except AttributeError:
        return handler.bad_request("error")