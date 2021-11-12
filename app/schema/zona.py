class ZonaSchema(object):
    
    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj)
        
    @classmethod
    def _serialize_collection(cls, collection):
        return{
            "zonas":[cls._serialize(item) for item in collection.items],
            "total":collection.total,
            "pagina":collection.page,
        }
        
    @classmethod
    def _serialize(cls, obj):
        dict = {}
        for attr in obj.__table__.columns:
            if getattr(obj,"estado") == "publicado":
                if attr.name != "estado":
                    dict[attr.name]= getattr(obj, attr.name)
        return dict