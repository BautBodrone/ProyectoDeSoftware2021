import { Map } from "../js/MapSingleMarker.js";

const submitHandler = (event, map) => {
    if (map.marker) {
        latlng = map.marker.getLatLng();
        document.getElementById('lat').setAttribute('value',latlng.lat);
        document.getElementById('lng').setAttribute('value',latlng.lng);
    }
    else {
        event.preventDefault();
        alert('se debe ingresar un punto en el mapa.');
    }
}

const resetHandler = (event, map) => {
    if (map.marker) {
        map.marker.remove();
    }
}

window.onload = () => {
    const map = new Map({
        selector: 'mapid'
    });

    const form = document.getElementById('form-map');
    form.addEventListener('submit', (event) => submitHandler(event, map));
    form.addEventListener('reset', (event) => resetHandler(event, map));

}
