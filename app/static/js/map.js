import { Map } from "../js/MapSingleMarker.js";

const submitHandler = (event, map) => {
    if (document.getElementsByClassName('one-mark').length != 0){
        if (map.marker) {
            document.getElementById('lat').setAttribute('value',map.marker.getLatLng().lat);
            document.getElementById('lng').setAttribute('value',map.marker.getLatLng().lng);
        }
        else {
            event.preventDefault();
            alert('se debe ingresar un punto en el mapa.');
        }
    }
    else {
        if (map.marker_list.length > 2){
            document.getElementById('coordenadas').setAttribute('value',map.marker_list);
        }
        else {
            event.preventDefault();
            alert('se debe ingresar al menos tres puntos en el mapa.');
        }
    }
}

const resetHandler = (map , first_marker) => {
    if (first_marker !== undefined){
        map.addOneMarker(map.first_marker.getLatLng());
    }
    else{
        map.marker.remove();
    }
}

window.onload = () => {
    const map = new Map({
        selector: 'mapid'
    });

    if (document.getElementById('form-map') !== null){
        
        const form = document.getElementById('form-map');
   
        form.addEventListener('submit', (event) => submitHandler(event, map));
        form.addEventListener('reset', () => resetHandler(map, map.first_marker));
        if (document.getElementsByClassName('one-mark').length != 0){
            map.map.addEventListener('click', (e) => { map.addOneMarker(e.latlng); });
        } else {
            map.map.addEventListener('click', (e) => { map.addMarker(e.latlng); });
        }
    }
}
