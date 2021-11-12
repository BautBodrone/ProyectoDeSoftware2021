class ZonaSchema(object):
    
    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj,True)
        
    @classmethod
    def _serialize_collection(cls, collection):
        return {
            "zonas":[cls._serialize(item) for item in collection.items],
            "total":collection.total,
            "pagina":collection.page,
        }
        
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        dict = {}
        for attr in obj.__table__.columns:
            if getattr(obj,"estado") == "publicado" or oneObj:
                print( "=============================")
                print(attr.name)
                if attr.name == "coordenadas":
                    coordenadas = {}
                    list = []
                    lat_long = (getattr(obj, attr.name)).split(",")
                    for i in range(len(lat_long)):
                        if (i%2)==0:
                            coordenadas["latitud"]=lat_long[i]
                        else:
                            coordenadas["longitud"]=lat_long[i]
                            list.append(coordenadas)
                            coordenadas = {}
                    dict["coordenadas"]=list
                elif attr.name != "estado":
                    dict[attr.name]= getattr(obj, attr.name)
                
        return dict