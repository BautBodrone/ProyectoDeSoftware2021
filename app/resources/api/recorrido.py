from flask import jsonify, Blueprint, request, abort

from app.models.recorrido import Recorrido
from app.schema.recorridos import RecorridoSchema

from app.models.configuration import Configuration
from app.db import db
import collections

import app.helpers.handler as handler

from sqlalchemy import exc

recorrido_api = Blueprint("recorrido", __name__, url_prefix="/recorridos-evacuacion")

@recorrido_api.get("/")
def get():
    
    pagina = request.args.get("pagina","1")
    if pagina.isnumeric():
        conf = Configuration.query.first()
        zonas_page = Recorrido.query.paginate(page=int(pagina),per_page=conf.rows_per_page)
        atributos = RecorridoSchema.dump(zonas_page,many=True)
        
        return jsonify(atributos)
    else:
        handler.bad_request("error")
    
   
