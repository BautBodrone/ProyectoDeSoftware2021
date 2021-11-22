from flask import jsonify, Blueprint, request, abort

from app.models.denuncia import Denuncia
from app.db import db
import collections
from app.schema.denuncia import DenunciaSchema
import app.helpers.handler as handler

from sqlalchemy import exc


denuncias_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")


@denuncias_api.post("")
def create():
    try:
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
                print(atributos)
                print("==========================")
                return jsonify(atributos=atributos)
            else:
                return handler.range_not_satisfiable("error")
        else:
            raise AttributeError
    except AttributeError:
        return handler.bad_request("error")


