from flask import jsonify, Blueprint, request, abort

from app.models.denuncia import Denuncia
from app.db import db
import collections
from app.models.configuration import Configuration
from app.schema.denuncia import DenunciaSchema
import app.helpers.handler as handler

from sqlalchemy import exc


denuncias_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@denuncias_api.get("/")
def get():
    pagina = request.args.get("pagina","0")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        if pagina != "0":
            denuncias_page = Denuncia.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        else:
            denuncias_page = Denuncia.query.all()
        atributos = DenunciaSchema.dump(denuncias_page,pagina,many=True)
        
        return jsonify(atributos)
    else:
        handler.bad_request("error")
    
@denuncias_api.post("/")
def create():
    print("entro api")
    try:
        print("----------------------------Pido jsdon")
        print(request.get_json())
        denuncia_aux = DenunciaSchema.post_format(request.get_json())
        
        denuncia = Denuncia(**denuncia_aux)
        db.session.add(denuncia)
        try:
            db.session.commit()
            return jsonify(denuncia_aux)
        except exc.IntegrityError:
            return handler.server_error("error")
    except:
        return handler.bad_request("error")
    
@denuncias_api.get("/<id>")
def get_id(id):
    id=(id.replace(":",""))
    try:
        if id.isnumeric():
            denuncia = Denuncia.query.filter_by(id=id).first()
            if denuncia != None:
                atributos = DenunciaSchema.dump(denuncia)
                return jsonify(atributos=atributos)
            else:
                return handler.range_not_satisfiable("error")
        else:
            raise AttributeError
    except AttributeError:
        return handler.bad_request("error")


