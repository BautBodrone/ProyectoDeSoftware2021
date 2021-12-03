class ZonaSchema(object):
    
    @classmethod
    def dump(cls, obj, page=None, many=False):
        if many:
            return cls._serialize_collection(obj,page)
        else:
            return cls._serialize(obj,True)
        
    @classmethod
    def _serialize_collection(cls, collection, page):
        if page!="0":
            return {
                "zonas":[cls._serialize(item) for item in collection.items],
                "total":collection.total,
                "pagina":collection.page,
            }
        else:
            return{
                "zonas":[cls._serialize(item) for item in collection],
                "total":len(collection)
            }
        
    @classmethod
    def _serialize(cls, obj, oneObj=False):
        dict = {}
        for attr in obj.__table__.columns:
            if getattr(obj,"estado") == "publicado" or oneObj:
                if attr.name == "coordenadas":
                    coordenadas = {}
                    list = []
                    lat_long = (getattr(obj, attr.name)).split(",")
                    for i in range(len(lat_long)):
                        if (i%2)==0:
                            coordenadas["lat"]=lat_long[i]
                        else:
                            coordenadas["lng"]=lat_long[i]
                            list.append(coordenadas)
                            coordenadas = {}
                    dict["coordenadas"]=list
                elif attr.name != "estado":
                    dict[attr.name]= getattr(obj, attr.name)
                
        return dict