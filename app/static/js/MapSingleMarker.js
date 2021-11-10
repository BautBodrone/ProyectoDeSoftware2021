const initialLat = -34.9186;
const initialLng = -57.956;
const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

export function Map({selector}) {
    let map;
    let marker;

    initializeMap(selector);
    
    map.addEventListener('click', (e) => { addMarker(e.latlng) });

    function initializeMap(selector) {
        map = L.map(selector).setView([initialLat, initialLng], 13);
        L.tileLayer(mapLayerUrl).addTo(map);
    };

    function addMarker({lat, lng}){
        if (marker) {
            marker.remove();
        };
        marker = L.marker([lat, lng]).addTo(map);
        map.setView([marker.getLatLng().lat, marker.getLatLng().lng], 13);
    };

}
