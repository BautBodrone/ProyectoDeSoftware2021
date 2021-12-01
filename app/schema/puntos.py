class PuntoSchema(object):
    
    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj,True)
        
    @classmethod
    def _serialize_collection(cls, collection):
        return {
            "puntos_encuentro":[cls._serialize(item) for item in collection.items],
            "total":collection.total,
            "pagina":collection.page,
        }
        
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        send = {}
        for attr in obj.__table__.columns:
            if attr.name == "id":
                send["id"] = cls._get_categoria_by_code(getattr(obj, attr.name))
            if attr.name == "nombre":
                send["nombre"] = getattr(obj, attr.name)
            if attr.name == "direccion":
                send["direccion"] = getattr(obj, attr.name)
            if attr.name == "lat":
                send["lat"] = getattr(obj, attr.name)
            if attr.name == "lng":
                send["lng"] = getattr(obj, attr.name)
            if attr.name == "telefono":
                send["telefono"] = getattr(obj, attr.name)
            if attr.name == "email":
                send["email"] = getattr(obj, attr.name)       
        return send
        
        
        
        
        
        