import collections  

class ConfigurationSchema(object):
    @classmethod
    def _get_Order(cls,id):
            opciones = {
                'prioridad': 'Prioridad',
                'cercania': 'cercania',
                'a..z': 'A..Z',
                'z..a': 'Z..A'}
            return opciones[id]
       
        
        
    @classmethod
    def dump(cls, obj):
        send = {}
        for attr in obj.__table__.columns:
            if attr.name == "rows_per_page":
                send["rows_per_page"] = getattr(obj, attr.name)
            if attr.name == "order":
                send["order"] = cls._get_Order(getattr(obj, attr.name))
            if attr.name == "public_bg_color":
                send["public_bg_color"] = getattr(obj, attr.name)
            if attr.name == "public_accent_color":
                send["public_accent_color"] = getattr(obj, attr.name)
            if attr.name == "public_letters_color":
                send["public_letters_color"] = getattr(obj, attr.name)
        return send