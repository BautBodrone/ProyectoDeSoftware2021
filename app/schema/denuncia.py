import collections

class DenunciaSchema(object):
    
    @classmethod
    def dump(cls, obj, page=None ,many=False):
        if many:
            return cls._serialize_collection(obj,page)
        else:
            return cls._serialize(obj,True)
        
    @classmethod
    def _serialize_collection(cls, collection, page):
        if page!="0":
            return {
                "denuncias":[cls._serialize(item) for item in collection.items] ,
                "total": collection.total,
                "pagina": collection.page
            }
        else:
            return{
                "recorridos":[cls._serialize(item) for item in collection],
                "total":len(collection)
            }
            
    @classmethod
    def _get_categoria_by_id(cls,id):
        if (id > 0 and id < 4):
            opciones = {
                1:'cañeria_rota',
                2: 'calle_inundable',
                3: 'calle_rota',
                4: 'otro'}
            return opciones[id]
        else:
            raise 404
        
    @classmethod
    def _get_categoria_by_code(cls,code):
        opciones = {
                'Cañeria Rota':1,
                'Calle Inundable':2,
                'Calle Rota':3,
                'Otro':4}
        code = str(code)
        return opciones[code]
        
    @classmethod
    def _parse_coordenadas(cls,coords):
        lat_long = coords.split(",")
        return (lat_long)
        
    @classmethod
    def post_format(cls,dict):
        base = ['categoria_id', 'coordenadas', 'apellido_denunciante', 'nombre_denunciante',
                'telcel_denunciante', 'email_denunciante', 'titulo', 'descripcion']
        if (collections.Counter(base) == collections.Counter(dict.keys())):
            send = {}
            send["categoria"] = cls._get_categoria_by_id(dict['categoria_id'])
            lat_long = cls._parse_coordenadas(dict["coordenadas"])
            send["lat"] = lat_long[0]
            send["lng"] = lat_long[1]
            send["apellidoD"] = dict["apellido_denunciante"]
            send["nombreD"] = dict["nombre_denunciante"]
            send["telefono"] = dict["telcel_denunciante"]
            send["emailD"] = dict["email_denunciante"]
            send["titulo"] = dict["titulo"]
            send["descripcion"] = dict["descripcion"][:30]
            send["estado"] = "curso"
            send["asignadoA"] = 1
            return send
        else:
            raise
        
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        send = {}
        for attr in obj.__table__.columns:
            if attr.name == "categoria":
                send["categoria_id"] = cls._get_categoria_by_code(getattr(obj, attr.name))
            if attr.name == "lat":
                send["lat"] = getattr(obj, attr.name)
            if attr.name == "lng":
                send["lng"] = getattr(obj, attr.name)
            if attr.name == "apellidoD":
                send["apellido_denunciante"] = getattr(obj, attr.name)
            if attr.name == "nombreD":
                send["nombre_denunciante"] = getattr(obj, attr.name)
            if attr.name == "telefono":
                send["telcel_denunciante"] = getattr(obj, attr.name)
            if attr.name == "emailD":
                send["email_denunciante"] = getattr(obj, attr.name)
            if attr.name == "titulo":
                send["titulo"] = getattr(obj, attr.name)
            if attr.name == "descripcion":
                send["descripcion"] = getattr(obj, attr.name)
            if attr.name == "descripcion":
                send["descripcion"] = getattr(obj, attr.name)
        return send