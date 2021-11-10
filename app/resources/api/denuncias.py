from flask import jsonify, Blueprint, request, abort

#from app.models.denuncias import Denuncias

denuncias_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")


@denuncias_api.post("/:")
def post(id):
    
    denuncia = request.data
    try:
        Denuncias.save(denuncia)
    except IntegrityError:
        abort(400)
    except:
        abort(500) 
    return jsonify(denuncia=denuncia)
