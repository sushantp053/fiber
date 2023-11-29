var map = L.map('map', {
    center: [
        17.04731465553872, 74.26828304407233],
    zoom: 13
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
// 	maxZoom: 19,
// 	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);

const markers = JSON.parse(
    document.getElementById('django_data').textContent
  );

  var replacer = function(key, value) {
    return typeof value === 'undefined' ? null : value;
  }
    var d = document.getElementById('talav_data').textContent
    var talav = JSON.parse(d);
    var talavData = JSON.parse(talav.data)
    console.log(talavData)
    

    markers.forEach(element => {
        L.marker([element.lat, element.lng]).addTo(map);
    });

    talavData.features.forEach(element => {
        let latlngs = []
        element.geometry.coordinates[0][0].forEach(points => {
            let a = [points[1], points[0]]
            latlngs.push(a)
        })
        if(element.properties.area >= "400"){
        L.polyline(latlngs, {color: 'red'}).addTo(map);

    }else if (element.properties.area >= "200"){
        L.polyline(latlngs, {color: 'blue'}).addTo(map);
    } else {
        L.polyline(latlngs, {color: 'yellow'}).addTo(map);
    }
        
    })


    



