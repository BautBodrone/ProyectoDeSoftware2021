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

const resetHandler = (map) => {
    
    console.log(map.marker.getLatLng());
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
    form.addEventListener('reset', () => resetHandler(map));
    console.log(map);
    console.log(map.marker);
}
