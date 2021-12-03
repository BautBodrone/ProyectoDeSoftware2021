class PuntoSchema(object):
    
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
                "puntos_encuentro":[cls._serialize(item) for item in collection.items],
                "total": collection.total,
                "pagina": collection.page
            }
        else:
            return{
                "puntos_encuentro":[cls._serialize(item) for item in collection],
                "total":len(collection)
            }
            
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        send = {}
        for attr in obj.__table__.columns:
            if attr.name == "id":
                send["id"] = getattr(obj, attr.name)
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
        
        
        
        
        
        