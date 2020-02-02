var weights = JSON.parse('[[[-3.5768745,-0.9146297,-0.8281121,0.08896488,-0.9816154,-0.33906782,1.7328273,-0.8788098,0.82919645,-0.8502152,-0.6819073,0.9832589,-2.0255966,2.238618,-3.1949744,-1.1375612,1.2710911,-0.08632089,-0.57707137,-2.3211594],[0.19185102,-0.29176295,-2.8088207,0.00644564,-2.8117127,0.09334402,0.00915366,0.10100973,-0.07510929,0.11060901,-0.6761018,-1.3463391,-1.7854781,-1.9636552,0.07501592,-2.2802732,-1.8074472,-2.5219393,-2.1542482,-0.13825691],[3.8458033,-0.98417825,1.5193231,0.7128726,0.912387,1.998151,2.1136189,-0.85771656,2.7413633,1.2620711,0.6156211,1.8754215,2.0417247,0.26895037,0.42322728,4.289314,2.6801436,1.5265828,2.258736,2.1424875],[-2.3191617,-0.04371871,-0.8964422,-0.8142232,1.5459852,1.044404,-0.16068263,1.5828046,3.1913247,0.25733128,2.009446,-1.0909529,-1.9339036,-1.8330642,0.3213526,1.4466655,-2.8607974,2.2667906,2.712904,1.2198309],[-2.035814,1.1404011,1.2035809,-2.5417163,1.5025697,0.97223264,3.9333918,1.8558053,1.2185203,0.49972662,1.2196491,1.5792463,1.5447621,-0.00486948,2.6083264,-1.7151024,-2.0557015,-1.3465414,0.7808735,-0.3919436],[-1.250192,-2.180262,-0.66968596,-1.1291883,-1.6948779,-1.3897471,2.0885074,-1.0506437,1.2196226,-3.0932717,0.06161784,1.124809,-0.37377945,-0.15622798,-2.2706006,2.1617877,-0.29563725,0.38655168,-0.5956604,-0.5639549],[-1.1448185,-0.21598202,0.23216297,2.9623115,1.936638,0.56289726,-3.2221236,-1.1395787,-1.4139326,1.0253668,-2.7908828,-1.7798271,-1.2260389,-0.1619513,-0.14438637,0.07487026,1.1599909,-0.90494424,-0.1202907,0.402994],[-1.5885324,-2.3190405,-0.54914224,-2.1873214,0.22866212,0.12272029,0.0956087,-1.7827653,1.6180178,1.4666225,-0.7104454,-1.8296813,0.3747058,-1.205941,-2.040706,-0.02051357,0.13824847,-1.8989692,0.22984895,0.27714938],[-0.40110794,-1.4445093,3.3337104,1.9687929,-2.322593,-1.3728576,0.5603248,-1.0272853,-0.6077586,0.9599089,1.5957822,0.88893956,1.8314805,-1.721326,-0.24741742,0.68213004,2.288255,0.5876136,3.3511922,-2.0180109],[-2.9528515,-2.9322822,-1.4003211,0.6865122,0.35275885,-1.566079,-0.04184283,-3.8168364,1.3103918,-0.5325101,0.2348131,-0.712767,-0.8099319,-0.9696461,-0.47024006,0.4776768,-0.21909915,-1.0106049,-0.06654783,-0.43005016],[0.6421338,2.016935,0.82651466,-1.6314356,0.05836394,3.6236336,-1.2763782,0.89951646,-1.3122399,-0.9065607,-0.6444648,-0.5192291,-1.9375618,-1.7817861,-0.1925668,1.5991669,-0.5049134,-1.5982238,-1.500255,-1.1498077]],[-0.2843259,-0.05496123,-0.25661436,-0.064958,-0.0840142,-0.04584642,0.06902491,-0.00608902,0.12158661,0.07344336,-0.36598438,-0.25315213,-0.0907021,0.25604036,0.15290314,-0.09695873,-0.12861569,-0.01566326,-0.07609668,0.29331368],[[-0.05245389],[-0.10447218],[-1.0968732],[-0.08963237],[-0.2779294],[-0.00698484],[0.01275865],[0.06453738],[0.02688908],[-0.02345005],[-1.4964247],[-0.83364254],[-0.450754],[0.92418545],[-0.00204538],[0.00289212],[0.00394645],[-0.07127646],[-0.24781457],[1.0741601]],[0.2693744]]')
var countyConversionTable = JSON.parse('{"Los Angeles": 17, "San Diego": 35, "Orange": 28, "Riverside": 31, "San Bernardino": 34, "Santa Clara": 40, "Alameda": 0, "Sacramento": 32, "Contra Costa": 6, "Fresno": 9, "Kern": 13, "Ventura": 53, "San Mateo": 38, "San Joaquin": 36, "Stanislaus": 47, "Sonoma": 46, "Tulare": 51, "Solano": 45, "Santa Barbara": 39, "Monterey": 25, "Placer": 29, "San Luis Obispo": 37, "Merced": 22, "Santa Cruz": 41, "Marin": 19, "Butte": 3, "Yolo": 54, "El Dorado": 8, "Shasta": 42, "Madera": 18, "Kings": 14, "Napa": 26, "Humboldt": 11, "Nevada": 27, "Sutter": 48, "Mendocino": 21, "Yuba": 55, "Lake": 15, "Tehama": 49, "San Benito": 33, "Tuolumne": 52, "Calaveras": 4, "Siskiyou": 44, "Amador": 2, "Lassen": 16, "Glenn": 10, "Del Norte": 7, "Colusa": 5, "Plumas": 30, "Inyo": 12, "Mariposa": 20, "Mono": 24, "Trinity": 50, "Modoc": 23, "Sierra": 43, "Alpine": 1, "Imperial": -1, "San Francisco": -1}')



let map;
var marker;
var circle;
var magnitude = 200000;

unresolved = {
    timer: [],
    interval: []
};

function clearMap() {
    for (var i of unresolved.timer) {
        clearTimeout(i);
    }
    for (var i of unresolved.interval) {

        clearInterval(i);
    }
    if (marker) {
        marker.setMap(null);
    }
    if (circle) {
        circle.setMap(null);
    }
    unresolved = {
        timer: [],
        interval: []
    };

}

function timeout(func, time) {
    var id = setTimeout(function(e) {
        var index = unresolved.timer.indexOf(id);
        if (index > -1) {
            unresolved.timer.splice(index, 1);
        }
        func(e);
    }, time);
    unresolved.timer.push(id);
    return id;
}



function initMap() {
    clearMap();
    var california = {
        lat: 36.778259,
        lng: -119.417931
    };
    map = new google.maps.Map(document.getElementById('map'),{
        zoom: 6,
        center: california
    });
    var geocoder = new google.maps.Geocoder();
    map.addListener('click', function(e) {
        addMarker(e.latLng);
    });
    var input = document.getElementById('pac-input');
    var searchBox = new google.maps.places.SearchBox(input);
    searchBox.addListener('places_changed', function() {
        //           console.log("say something");
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }
        var goal = places[0];

        console.log(places);
        map.panTo(goal.geometry.location);
        addMarker(goal.geometry.location);

    });

}

function addMarker(latLng) {
    clearMap();
    document.getElementById('longtitude').value = latLng.lng();
    document.getElementById('latitude').value = latLng.lat();
    getCounty(latLng.lat(), latLng.lng());

    marker = new google.maps.Marker({
        map: map,
        position: latLng,
        animation: google.maps.Animation.BOUNCE,
        icon: {
            size: new google.maps.Size(50,50),
            scaledSize: new google.maps.Size(50,50),
            url: "fire2.png"
        }
    });
    
    // timeout(function(e) {
    //     // getCircle(latLng);
    //     marker.setMap(null);
    //     //change magnitude
    // }, 1500)
    // triggerCalculation(latLng.lat(), latLng.lng());

    return marker

}
function getCounty(latitude, longtitude) {
    //     console.log(latitude, longtitude);
    var latlng = new google.maps.LatLng(latitude,longtitude);
    var geocoder = new google.maps.Geocoder();
    var county;
    geocoder.geocode({
        'latLng': latlng
    }, function(results, status) {
        if (status !== google.maps.GeocoderStatus.OK) {
            alert(status);
        }
        // This is checking to see if the Geoeode Status is OK before proceeding
        if (status == google.maps.GeocoderStatus.OK) {
            //             console.log(results);
            var addressarray = (results[0].address_components);
            for (var i in addressarray) {
                var typearray = addressarray[i].types;
                if (typearray[0] == "administrative_area_level_2") {
                    var temp = addressarray[i].long_name.split(" ");
                    temp.pop();
                    console.log(temp.join(" "))
                    document.getElementById('county').value = temp.join(" ");
                }
            }
        }

    });

}

function getCircle(magnitude, latLng, callback) {
    generateCirclenimation(0.75, magnitude, latLng, callback);

}

function generateCirclenimation(seconds, magnitude, center, callback) {
    var interval = 25;
    var step = 0;
    var max = seconds * 1000 / interval;
    var maxRadius = Math.sqrt(magnitude * 4046.86);
    if (circle != null) {
        circle.setMap(null);
    }
    circle = new google.maps.Circle({
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#FF0000',
        fillOpacity: 0.35,
        map: map,
        center: center,
        radius: 0
    });
    var i = setInterval(function(e) {
        circle.setRadius(maxRadius * step / max);
        if (step++ == max) {
            clearInterval(i);
            map.fitBounds(circle.getBounds());
            callback && callback();
        }
    }, interval);
}

function calculatefunc(){
    var county = countyConversionTable[document.getElementById("county").value];
    var month = document.getElementById("month").selectedIndex + 1;
    var maxTemp = document.getElementById("max T").value;
    var minTemp = document.getElementById("min T").value;
    var maxHum = document.getElementById("max H").value;
    var minHum = document.getElementById("min H").value;
    var direction = document.getElementById("direction").selectedIndex + 1;
    var windspeed = document.getElementById("windspeed").value;
    var precipitation = document.getElementById("percipitation").value;
    var longtitude = document.getElementById("longtitude").value;
    var latitude = document.getElementById("latitude").value;
    var dataArr = [county,latitude,longtitude,month,precipitation,maxTemp,minTemp,direction,windspeed,maxHum,minHum];
    if (dataArr.filter(function (x) {return x === ''}).length > 0) {
        alert('Please fill out all the fields!');
        return;
    }
    if (county===void 0) {
        alert('Selected region is not in California! Please try somewhere else.');
        return;
    }
    var result = applyModel(dataArr.map(parseFloat));
    getCircle(result, marker.position, function(e) {

        // marker.setMap(null)
    });
    var contentString = result.toFixed(2) + " acres";
    var infowindow = new google.maps.InfoWindow({
        content : contentString
    });
    infowindow.open(map,marker);

}


function transpose(array) {
    
    return array[0].map((col, i) => array.map(row => row[i]));
}

function dotProduct(x, y) {
    if (x.length !== y.length) {
        alert('Type Mismatch!');
        throw('dot');
    }
    out = 0;
    for (var i in x) {
        out += x[i] * y[i];
    }
    return out;
}

function addition(x, y) {
    if (x.length !== y.length) {
        alert('Type Mismatch!');
        throw('add');
    }
    var out = []
    for (var i in x) {
        out.push(x[i] + y[i]);
    }
    return out;
}

function matrixMul(X, y) {
    var out = [];
    for (var i in X) {
        out.push(dotProduct(X[i], y));
    }
    return out;
}

function applyModel(a) {
    var calc = addition(weights[3], 
    matrixMul(transpose(weights[2]), addition(weights[1], elu(matrixMul(transpose(weights[0]), a)))))[0];
    return Math.exp(calc);
}
function elu(vec) {
    return vec.map(function(m) {return m < 0 ? Math.exp(m) - 1 : m})
}