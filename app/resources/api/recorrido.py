from flask import jsonify, Blueprint, request, abort

from app.models.recorrido import Recorrido
from app.schema.recorridos import RecorridoSchema
from app.db import db
import collections

import app.helpers.handler as handler

from sqlalchemy import exc

recorrido_api = Blueprint("recorrido", __name__, url_prefix="/recorridos-evacuacion")

@recorrido_api.get("/")
def get():
    rec = Recorrido.query.all()
    print (rec)
    if rec != None:
        recorrido = RecorridoSchema.dump(rec, many=True)
        return jsonify(recorrido=recorrido)
    else:
        return handler.bad_request("error")

