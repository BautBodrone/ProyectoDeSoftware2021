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
        let coordenadas = document.getElementById('zonas').value;
        coordenadas = this.parseToArray(coordenadas);
        let color = document.getElementById('zonascolores').value;
        let nombre = document.getElementById('nombre').value;
        this.addZone(coordenadas,color,nombre);
        this.map.fitBounds(this.#drawnItems.getBounds());
        
        alert(this.#drawnItems.getBounds());
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
        this.#drawnItems.remove();
        this.zona = '';
        createControls.addTo(map);
        editControls.remove();
    }

    hasValidZone(){
        return this.drawnLayers.lenght === 1;
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
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw: {
                circle: false,
                marker: false,
                polyline: false
            }
        });
    }
    
    addLine(linea, nombre){
        var polyline = L.polyline(
            linea,{color: 'green'}
        ).addTo(this.map).bindPopup(nombre);
        this.map.fitBounds(polyline.getBounds());
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
        this.zona = L.polygon(
            zona, {color:color}
        )
        this.zona.addTo(this.#drawnItems).bindPopup(nombre);
    }
}
const submitHandler = (event, map) => {
    alert(map.marker_list)
    if (map.marker_list.length > 2){
        document.getElementById('zonas').setAttribute(map.marker_list);
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

