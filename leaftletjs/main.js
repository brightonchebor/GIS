window.onload = init;

function init() {

    const mapElement = document.getElementById('mapid')

    const openStreetMapStandard = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
        {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}
    )

    const mymapp = L.map('mapid', {
        center: [48, 14],
        zoom: 4,
        minZoom: 4,
        zoomSnap: 0.25,
        zoomDelta: 0.25,
        easeLinearity: 0.5,
        layers : [
            openStreetMapStandard
        ]
    })
    
    mymapp.on('zoom', function(e){
        console.log(e.target._zoom)
    })

    const baseLayers = {
        'openStreetMapStandard':openStreetMapStandard,
    }

    const layerControls = L.control.layers(
        baseLayers, {}, {}
    ).addTo(mymapp)

    mymapp.on('click', function(event){
        console.log(event.latlng)
    })

    // Marker
    const pathMarker = L.marker({lat: 48.545705491847464, lng: 12.656250000000002}).addTo(mymapp)
}