window.onload = init;

function init() {

    const mapElement = document.getElementById('mapid')

    const openStreetMapStandard = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
        {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}
    )

    const mymapp = L.map('mapid', {
        center: [48, 14],
        zoom: 4,
        layers : [
            openStreetMapStandard
        ]
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
}