from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.puntos import PuntoSchema
from app.models.punto import Punto
from app.models.configuration import Configuration
import app.helpers.handler as handler

puntos_api = Blueprint("puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@puntos_api.get("/")
def get():
    
    pagina = request.args.get("pagina","0")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        if pagina!="0":
            puntos = Punto.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        else:
            puntos = Punto.publicados()
        atributos = PuntoSchema.dump(puntos,pagina,many=True)
        
        return jsonify(atributos)
    else:
        handler.bad_request("error")
    
    
    
    

