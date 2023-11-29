var map = L.map("map", {
  center: [17.31272258513325, 73.88772606233213],
  zoom: 15,
});

var pLineGroup = L.layerGroup();

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "© OpenStreetMap",
}).addTo(map);

// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
// 	maxZoom: 19,
// 	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);

const markers = JSON.parse(document.getElementById("django_data").textContent);

var replacer = function (key, value) {
  return typeof value === "undefined" ? null : value;
};
var d = document.getElementById("talav_data").textContent;
var natoshi = JSON.parse(d);
var natoshiData = JSON.parse(natoshi.data);
console.log(natoshiData);

markers.forEach((element) => {
  L.marker([element.lat, element.lng]).addTo(map);
});

function changeCrop(crop) {
  pLineGroup.removeFrom(map);
  pLineGroup.clearLayers();
  console.log(crop);
  if (crop == "All Crop") {
    showAllCrop();
  } else {
    showSelectedCrop(crop);
  }
}
function showSelectedCrop(name) {
  natoshiData.features.forEach((element) => {
    let latlngs = [];
    element.geometry.coordinates[0][0].forEach((points) => {
      let a = [points[1], points[0]];
      latlngs.push(a);
    });
    if (element.properties.crop == name) {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "yellow",
          weight: 1,
          fillColor: "green",
          fill: true,
        })
      );
    }
  });
  pLineGroup.addTo(map);
}
function showAllCrop() {
  natoshiData.features.forEach((element) => {
    let latlngs = [];
    element.geometry.coordinates[0][0].forEach((points) => {
      let a = [points[1], points[0]];
      latlngs.push(a);
    });
    if (element.properties.crop == "Sugar Cane") {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "yellow",
          weight: 1,
          fillColor: "green",
          fill: true,
        })
      );
    } else if (element.properties.crop == "Barren") {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "yellow",
          weight: 1,
          fillColor: "orange",
          fill: true,
        })
      );
    } else if (element.properties.crop == "Cabbage") {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "yellow",
          weight: 1,
          fillColor: "blue",
          fill: true,
        })
      );
    } else if (element.properties.crop == "Ground Nut") {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "orange",
          weight: 1,
          fillColor: "pink",
          fill: true,
        })
      );
    } else if (element.properties.crop == "Mango") {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "green",
          weight: 1,
          fillColor: "green",
          fill: true,
        })
      );
    } else {
      pLineGroup.addLayer(
        L.polygon([latlngs], {
          color: "yellow",
          weight: 1,
          fillColor: "white",
          fill: true,
        })
      );
    }
  });
  pLineGroup.addTo(map);
}

showAllCrop();

var totalCrop = parseInt(document.getElementById("totalCrop").innerHTML);
var d = document.getElementsByClassName("bar");
for (let element of d) {
  let count = parseInt(element.innerHTML);
  let per = (count / totalCrop) * 100;
  element.style.width = per + "%";
  element.innerHTML = parseFloat(per).toFixed(4);
}
