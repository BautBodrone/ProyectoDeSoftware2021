class RecorridoSchema(object):
    
    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj,True)
        
    @classmethod
    def _serialize_collection(cls, collection):
        return {
            "recorridos":[cls._serialize(item) for item in collection.items],
            "total":collection.total,
            "pagina":collection.page,
        }
        
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        send = {}
        for attr in obj.__table__.columns:
            if attr.name == "id":
                send["id"] = getattr(obj, attr.name)
            if attr.name == "nombre":
                send["nombre"] = getattr(obj, attr.name)
            if attr.name == "coordenadas":
                coordenadas = {}
                list = []
                lat_long = (getattr(obj, attr.name)).split(",")
                for i in range(len(lat_long)):
                    if (i%2)==0:
                         coordenadas["lat"]=lat_long[i]
                    else:
                        coordenadas["long"]=lat_long[i]
                        list.append(coordenadas)
                        coordenadas = {}
                send["coordenadas"]=list
            if attr.name == "descripcion":
                send["descripcion"] = getattr(obj, attr.name)      
        return send

        
        