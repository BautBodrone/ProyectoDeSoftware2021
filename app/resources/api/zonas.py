from flask import jsonify, Blueprint

#from app.models.zonas import Zonas

zonas_api = Blueprint("zonas-inundables", __name__, url_prefix="/zonas-inundables")


@zonas_api.get("/")
def index():
    
    zonas = Zonas.query.all()

    return jsonify(zonas=zonas)

@zonas_api.get("/:")
def get_id(id):
    
    zona = Zonas.query.filter_by(id=int(id)).first()

    return jsonify(zona=zona)
