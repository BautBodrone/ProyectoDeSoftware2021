import { Map } from "../js/MapSingleMarker.js";

const submitHandler = (event, map) => {
    if (map.marker) {
        document.getElementById('lat').setAttribute('value',map.marker.getLatLng().lat);
        document.getElementById('lng').setAttribute('value',map.marker.getLatLng().lng);
    }
    else {
        event.preventDefault();
        alert('se debe ingresar un punto en el mapa.');
    }
}

const resetHandler = (map , first_marker) => {
    if (map.marker != first_marker) {
        map.addMarker(first_marker);
    }
}

window.onload = () => {
    const map = new Map({
        selector: 'mapid'
    });

    const form = document.getElementById('form-map');
   
    form.addEventListener('submit', (event) => submitHandler(event, map));
    form.addEventListener('reset', () => resetHandler(map, map.first_marker));
}
