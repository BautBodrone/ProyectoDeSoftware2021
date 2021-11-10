from app.models import coordenada
from app.models.coordenada import Coordenada

def search_coordenada(id):
    coordenada = Coordenada.search_coordenada(id)
    return coordenada