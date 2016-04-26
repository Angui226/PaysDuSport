$(function() {
    var map = new GMaps({
                    div: '#maps',
                    lat: parseFloat(latitude),
                    lng: parseFloat(longitude),
                    width: '100%',
                    height: '500px',
                    zoom: 14,
                    zoomControl: true,
                    zoomControlOpt: {
                        style: 'SMALL',
                        position: 'TOP_LEFT'
                    },
                    panControl: false
                });
                
    map.addMarker({
        lat: parseFloat(latitude),
        lng: parseFloat(longitude)
    });
});