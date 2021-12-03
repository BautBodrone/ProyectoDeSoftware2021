from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.puntos import PuntoSchema
from app.models.punto import Punto
from app.models.configuration import Configuration
import app.helpers.handler as handler

puntos_api = Blueprint("puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@puntos_api.get("/")
def get():
    
    pagina = request.args.get("pagina","1")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        zonas_page = Punto.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        atributos = PuntoSchema.dump(zonas_page,many=True)
        
        return jsonify(atributos)
    else:
        handler.bad_request("error")
    
    
    
    

