from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.zona import ZonaSchema
from app.models.zona import Zona
from app.models.configuration import Configuration
import app.helpers.handler as handler

zonas_api = Blueprint("zonas-inundables", __name__, url_prefix="/zonas-inundables")


@zonas_api.get("/")
def index():
    
    pagina = request.args.get("pagina","0")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        if pagina!="0":
            zonas = Zona.query.paginate(page=int(pagina),per_page=conf.rows_per_page)    
        else:
            zonas = Zona.publicados()
        atributos = ZonaSchema.dump(zonas,pagina,many=True)
        return jsonify(atributos)
    else:
        handler.bad_request("error")

@zonas_api.get("/<id>")
def get_id(id):
    id=(id.replace(":",""))
    try:
        if id.isnumeric():
            zona = Zona.query.filter_by(id=id).first()
            if zona != None:
                
                atributos = ZonaSchema.dump(zona)
                return jsonify(atributos=atributos)
            else:
                return handler.range_not_satisfiable("error")
        else:
            raise AttributeError
    except AttributeError:
        return handler.bad_request("error")
