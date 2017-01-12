/**
 * Created by yaki on 11.01.17.
 */

function myMap() {
    var mapCanvas = document.getElementById("map");
    var london = new google.maps.LatLng(52.520008, 13.404954);
    var mapOptions = {
        center: london,
        zoom: 10
    };
    var map = new google.maps.Map(mapCanvas, mapOptions);
    var marker = new google.maps.Marker({position: london});

    google.maps.event.addListener(map, 'click', function (event) {
        marker.setMap(null);
        marker = placeMarker(event.latLng, map);
    });
    google.maps.event.addListener(map, 'mousemove', function (e) {
        map.setOptions({draggableCursor: 'pointer'});
    });
}

function placeMarker(location, map) {
    return new google.maps.Marker({
        position: location,
        map: map
    });
}