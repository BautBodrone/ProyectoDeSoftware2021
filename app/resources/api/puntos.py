from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.puntos import PuntoSchema
from app.models.punto import Punto
from app.models.configuration import Configuration
import app.helpers.handler as handler

puntos_api = Blueprint("puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@puntos_api.get("/")
def get():
    punto = Punto.query.all()
    print (punto)
    if punto != None:
        puntos = PuntoSchema.dump(punto, many=True)
        return jsonify(puntos=puntos)
    else:
        return handler.bad_request("error")
    
    

