const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export class NewAndEditZona {
    #drawnItems;
    
    constructor({selector}, zone) {
        this.#drawnItems = new L.FeatureGroup();
        alert(zone)
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
        //coordenadas = this.parseToArray(coordenadas);
        //this.#drawnItems.push()
        this.map.addLayer(this.#drawnItems);
        
        this.map.addControl(this.createControls);
    }

    #eventHandler(e, map, drawnItems, editControls, createControls){
        const existingZones = Object.values(drawnItems._layers);

        if (existingZones.length == 0){
            const layer = e.layer;

            layer.editing.enable();
            drawnItems.addLayer(layer);
            editControls.addTo(map);
            createControls.remove();
        }
    }

    #deleteHandler(map, editControls, createControls){
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
            this.parsed.push([aux[i],aux[i+1]]);
        }
        return parsed;
    }
    addZone(zona, color, nombre){
        var polygon = L.polygon(
            zona, {color:color}
        ).addTo(this.map).bindPopup(nombre);
        this.map.fitBounds(polygon.getBounds());
    }
}

