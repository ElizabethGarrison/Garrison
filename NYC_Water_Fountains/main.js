// Initialize the map
var mymap = L.map('mapid').setView([40.7128, -74.006], 10);

// Add the tile layer
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZWdhcnIiLCJhIjoiY2xobndxZHBiMGY3bDNkbWhwNHdxbmhuYiJ9.FW6859zjXoOn1vaLpWk0ig'
}).addTo(mymap);

// Load the data and add markers to the map
Promise.all([
  d3.csv("../data/DrinkingFountains_20190417.csv", d3.autoType),
]).then(function(data) {
    var markers = L.markerClusterGroup();
    data[0].forEach(function(d) {
        var marker = L.marker([d.LATITUDE, d.LONGITUDE]);
        if (d.TYPE == 'A') {
            marker.setIcon(L.icon({
                iconUrl: 'images/rectangular-fountain.png',
                iconSize: [30, 30]
            }));
        } else if (d.TYPE == 'B') {
            marker.setIcon(L.icon({
                iconUrl: 'images/circular-fountain.png',
                iconSize: [30, 30]
            }));
        } else if (d.TYPE == 'C') {
            marker.setIcon(L.icon({
                iconUrl: 'images/circular-fountain-overhang.png',
                iconSize: [30, 30]
            }));
        } else if (d.TYPE == 'D') {
            marker.setIcon(L.icon({
                iconUrl: 'images/rectangular-fountain-overhang.png',
                iconSize: [30, 30]
            }));
        } else if (d.TYPE == 'E') {
            marker.setIcon(L.icon({
                iconUrl: 'images/wheelchair-fountain.png',
                iconSize: [30, 30]
            }));
        } else if (d.TYPE == 'F') {
            marker.setIcon(L.icon({
                iconUrl: 'images/water-bottle.png',
                iconSize: [30, 30]
            }));
        } else {
            marker.setIcon(L.icon({
                iconUrl: 'images/default.png',
                iconSize: [30, 30]
            }));
        }
        marker.bindPopup("<b>" + d.FEATURESTA + "</b><br>" + d.DESCRIPTION);
        markers.addLayer(marker);
    });
    mymap.addLayer(markers);
});

