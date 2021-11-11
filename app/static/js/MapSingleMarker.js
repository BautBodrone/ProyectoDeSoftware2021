const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export class Map {
    constructor({ selector }) {

        this.initializeMap(selector);
        this.marker_list = [];
    }
    initializeMap(selector) {
        this.map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.addMarkersAndZones();
    };
    
    addMarkersAndZones(){
        if (document.getElementById('lat') != null){
            let puntosLat = document.getElementsByClassName('lat');
            let puntosLng = document.getElementsByClassName('lng');
            for (let i = 0; i < puntosLat.length; i++) {
                if ((puntosLat[i].value != '') && (puntosLng[i].value != '')){
                    this.first_marker = L.marker([puntosLat[i].value, puntosLng[i].value]).addTo(this.map);
                }
            }
        }
        if (document.getElementsByClassName('zonas') != null){
            let zonas = document.getElementsByClassName('zonas');
            let colores = document.getElementsByClassName('zonas-colores');
            for (let i = 0; i < zonas.length; i++) {
                let color = colores[i].value;
                let coordenadas = zonas[i].value.split(",");
                let zona = [];
                for (var j = 0; j < coordenadas.length; j=j+2) {
                    let coordenada = [];
                    coordenada.push(coordenadas[j],coordenadas[j+1]);
                    zona.push(coordenada);
                }
                this.addZone(zona,color);
            }
        }
    }

    addZone(zona,color){
        L.polygon(
            zona, {color:color}
        ).addTo(this.map);
    }

    addOneMarker({ lat, lng }) {
        if (this.marker) {
            this.marker.remove();
        }
        if (this.first_marker) {
            this.first_marker.remove();
        }
        this.marker = L.marker([lat, lng]).addTo(this.map);
        this.map.setView([this.marker.getLatLng().lat, this.marker.getLatLng().lng], 13);
    };
    
    addMarker({ lat, lng }) {
        this.marker = L.marker([lat, lng]).addTo(this.map);
        this.marker_list.push([this.marker.getLatLng().lat,this.marker.getLatLng().lng]);
        this.map.setView([this.marker.getLatLng().lat, this.marker.getLatLng().lng], 13);
    };
}
