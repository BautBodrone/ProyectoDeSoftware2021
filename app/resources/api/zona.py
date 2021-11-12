from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.zona import ZonaSchema
from app.models.zona import Zona
from app.models.configuration import Configuration
import app.helpers.handler as handler

zonas_api = Blueprint("zonas-inundables", __name__, url_prefix="/zonas-inundables")


@zonas_api.get("/")
def index():
    
    pagina = request.args.get("pagina","1")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        zonas_page = Zona.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        atributos = ZonaSchema.dump(zonas_page,many=True)
        
        return jsonify(atributos)
    else:
        handler.bad_request("error")

@zonas_api.get("/<id>")
def get_id(id):
    id=(id.replace(":",""))
    try:
        if id.isnumeric():
            print("+++++++++++++++++++++++++++++++++++++++")
            zona = Zona.query.filter_by(id=id).first()
            print(zona)
            if zona != None:
                
                atributos = ZonaSchema.dump(zona)
                return jsonify(atributos=atributos)
            else:
                print("+++++++++++++++++++++++++++++++++++++++")
                return handler.range_not_satisfiable("error")
        else:
            raise AttributeError
    except AttributeError:
        return handler.bad_request("error")
