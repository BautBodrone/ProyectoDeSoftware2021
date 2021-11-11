const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export class Map {
    constructor({ selector }) {

        this.initializeMap(selector);

        this.map.addEventListener('click', (e) => { this.addMarker(e.latlng); });
    }
    initializeMap(selector) {
        this.map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.addMarkersAndZones();
    };
    
    addMarkersAndZones(){
        if ((document.getElementById('lat').value != '') && (document.getElementById('lng').value != '')){
            this.first_marker = L.latLng((document.getElementById('lat').value), (document.getElementById('lng').value));
            this.addMarker(this.first_marker);
        };
        this.zones = document.getElementsByClass('zonas');
        for (zone in this.zones){
            this.addZone(zone);
        }
    }

    addZone(zone){
        L.polygon(
            zone
        ).addTo(mymap);
    }

    addMarker({ lat, lng }) {
        if (this.marker) {
            this.marker.remove();
        }
        this.marker = L.marker([lat, lng]).addTo(this.map);
        this.map.setView([this.marker.getLatLng().lat, this.marker.getLatLng().lng], 13);
    };
}
