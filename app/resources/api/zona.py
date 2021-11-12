from flask import jsonify, Blueprint, request
from flask.helpers import make_response

from app.schema.zona import ZonaSchema
from app.models.zona import Zona
from app.models.configuration import Configuration

zonas_api = Blueprint("zonas-inundables", __name__, url_prefix="/zonas-inundables")


@zonas_api.get("/")
def index():
    
    pagina = request.args.get("pagina","1")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        zonas_page = Zona.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        
        print("_____________________________________________")
        print("_____________________________________________")
        
        atributos = ZonaSchema.dump(zonas_page,many=True)
        
        return jsonify(atributos=atributos)
    else:
        kwargs = {
            "error_name": "400 Bad Request",
            "error_desciption": "Ingrese un numero",
        }
        return make_response("error.html",kwargs),400

@zonas_api.get("/<id>")
def get_id(id):
    id=(id.replace(":",""))
    if id.isnumeric():
        try:
            zona = Zona.query.filter_by(id=id).first()
            
            atributos = ZonaSchema.dump(zona)

            return jsonify(atributos=atributos)
        except AttributeError:
            kwargs = {
            "error_name": "400 Bad Request",
            "error_desciption": "Ingrese un numero",
            }
            return make_response("error.html",kwargs),400
