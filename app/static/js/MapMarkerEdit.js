const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export class NewAndEditZona {
    #drawnItems;
    
    constructor({selector}) {
        this.#drawnItems = new L.FeatureGroup();
        this.#initializeMap(selector);
        this.map.on(L.Draw.Event.CREATED, (e) => {
            this.#eventHandler(e, this.map, this.#drawnItems, this.editControls, this.createControls)
        });
        this.map.on('draw:deleted', () => {
            this.#deleteHandler(this.map, this.editControls, this.createControls)
        });
    }

    #initializeMap(selector){
        this.map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        let coordenadas = document.getElementById('coordenadas').value;
        let nombre = document.getElementById('nombre').value;
        coordenadas = this.parseToArray(coordenadas);   
        if (document.getElementById('zonascolores') != null){
            this.zonas = true;
            let color = document.getElementById('zonascolores').value;
            this.addZone(coordenadas,color,nombre);
        }
        else{
           this.addLine(coordenadas,nombre);
        }
        this.map.fitBounds(this.#drawnItems.getBounds());
        this.map.addLayer(this.#drawnItems);
        
        this.map.addControl(this.editControls);
    }

    #eventHandler(e, map, drawnItems, editControls, createControls){
        const existingZones = Object.values(this.#drawnItems._layers);
        
        if (existingZones.length == 0){
            const layer = e.layer;
            
            layer.editing.enable();
            drawnItems.addLayer(layer);
            editControls.addTo(map);
            createControls.remove();
        }
    }

    #deleteHandler(map, editControls, createControls){
        this.#drawnItems.clearLayers();
        createControls.addTo(map);
        editControls.remove();
    }

    hasValidZone(){
        return this.drawnLayers.length === 1;
    }

    get drawnLayers(){
        return Object.values(this.#drawnItems._layers);
    }

    get editControls(){
        return this.editControlsToolbar ||= new L.Control.Draw({
            draw: false,
            edit: {
                featureGroup: this.#drawnItems
            }
        });
    }

    get createControls(){
        if ( this.zonas ){
            return this.createControlsToolbar ||= new L.Control.Draw({
                draw: {
                    circle: false,
                    marker: false,
                    polyline: false
                }
            });
        }
        else{
            return this.createControlsToolbar ||= new L.Control.Draw({
                draw: {
                    circle: false,
                    marker: false,
                    polygon: false,
                    rectangle: false
                }
            });
        }
    }
    
    addLine(linea, nombre){
        L.polyline(
            linea,{color: 'green'}
        ).addTo(this.#drawnItems).bindPopup(nombre);
    }
    parseToArray(coordenadas){
        let aux = coordenadas.split(',');
        let parsed = []
        for (var i=0; i< aux.length; i=i+2){
            parsed.push([aux[i],aux[i+1]]);
        }
        return parsed;
    }
    addZone(zona, color, nombre){
        L.polygon(
            zona, {color:color}
        ).addTo(this.#drawnItems).bindPopup(nombre);
    }
}
const submitHandler = (event, map) => {
    if (map.hasValidZone()){
        var coordenadas = [];
        coordenadas = map.drawnLayers[0].getLatLngs().flat().map( coordenadas => {
            let aux = new String(coordenadas.lat)
            aux = aux +','+ coordenadas.lng
            return (aux)
        });
        document.getElementById('coordenadas').setAttribute('value',coordenadas);
    }
    else {
        event.preventDefault();
        alert('se debe ingresar al menos tres puntos en el mapa.');
    }
}
window.onload = () => {
    const map = new NewAndEditZona({
        selector: 'mapid'
    });
    const form = document.getElementById('form-map');
    form.addEventListener('submit', (event) => submitHandler(event, map));
}

