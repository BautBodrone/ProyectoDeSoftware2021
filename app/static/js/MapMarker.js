const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export class Map {
    constructor({ selector }) {

        this.marker_list = [];
        this.all_markers = [];
        this.initializeMap(selector);
        
    }
    initializeMap(selector) {
        this.map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
    };
    
    oneMarkerInit(){
        if (document.getElementsByClassName('punto-nombre') != null){
            let puntosNombre = document.getElementsByClassName('punto-nombre');
            let puntosLat = document.getElementsByClassName('punto-lat');
            let puntosLng = document.getElementsByClassName('punto-lng');
            for (let i = 0; i < puntosNombre.length; i++) {
                if ((puntosLat[i].value != '') && (puntosLng[i].value != '')){
                    this.first_marker = L.marker([puntosLat[i].value, puntosLng[i].value]);
                    this.addOneMarker(this.first_marker.getLatLng());
                    this.marker.bindPopup(puntosNombre[i].value);
                }
            }
        }
    }

    addMarkersAndZones(){
        if (document.getElementsByClassName('punto-lat') != null){
            let puntosNombre = document.getElementsByClassName('punto-nombre');
            let puntosLat = document.getElementsByClassName('punto-lat');
            let puntosLng = document.getElementsByClassName('punto-lng');
            for (let i = 0; i < puntosNombre.length; i++) {
                if ((puntosLat[i].value != '') && (puntosLng[i].value != '')){
                    this.marker = L.marker([puntosLat[i].value, puntosLng[i].value]);
                    this.addMarker(this.marker.getLatLng());
                    this.marker.bindPopup(puntosNombre[i].value);
                }
            }
        }
        if (document.getElementsByClassName('zonas') != null){
            let zonas = document.getElementsByClassName('zonas');
            let colores = document.getElementsByClassName('zonas-colores');
            let nombres = document.getElementsByClassName('zonas-nombre');
            for (let i = 0; i < zonas.length; i++) {
                let color = colores[i].value;
                let nombre = nombres[i].value;
                let coordenadas = zonas[i].value.split(",");
                let zona = [];
                for (var j = 0; j < coordenadas.length; j=j+2) {
                    let coordenada = [];
                    coordenada.push(coordenadas[j],coordenadas[j+1]);
                    zona.push(coordenada);
                }
                this.addZone(zona,color,nombre);
            }
        }
        if (document.getElementsByClassName('recorridos') != null){
            let recorridos = document.getElementsByClassName('recorridos');
            let nombres = document.getElementsByClassName('recorridos-nombre');
            for (let i = 0; i < recorridos.length; i++) {
                let nombre = nombres[i].value;
                let coordenadas = recorridos[i].value.split(",");
                let linea = [];
                for (var j = 0; j < coordenadas.length; j=j+2) {
                    let coordenada = [];
                    coordenada.push(coordenadas[j],coordenadas[j+1]);
                    linea.push(coordenada);
                }
                this.addLine(linea,nombre);
            }
        }
    }
    
    addLine(linea, nombre){
        var polyline = L.polyline(
            linea,{color: 'green'}
        ).addTo(this.map).bindPopup(nombre);
        this.map.fitBounds(polyline.getBounds());
    }

    addZone(zona, color, nombre){
        var polygon = L.polygon(
            zona, {color:color}
        ).addTo(this.map).bindPopup(nombre);
        this.map.fitBounds(polygon.getBounds());
    }

    addOneMarker({ lat, lng }) {
        if (this.marker) {
            this.marker.remove();
        }
        this.marker = L.marker([lat, lng]).addTo(this.map);
        this.map.setView([lat, lng], 13);
    };
    
    addMarker({ lat, lng }) {
        this.marker = L.marker([lat, lng]).addTo(this.map);
        this.marker_list.push([lat, lng]);
        this.all_markers.push(this.marker);
        this.map.setView([lat, lng], 13);
    };
}
