getBathValue = () => {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = parseInt(document.getElementById("uiSqft").value);

    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    location = "location_" + location
    var area = document.getElementById("uiArea_tpe").value;
    var areaArr = area.split(" ");
    area = "area_type_"
    for (let i = 0; i < areaArr.length - 1; i++) {
      area += areaArr[i] + " ";
    }
    area += " " + areaArr[areaArr.length - 1];
    var estPrice = document.getElementById("uiEstimatedPrice");

    let url = "http://127.0.0.1:5000/predict_home_price";

    data = {
      "total_sqft": sqft,
      "bhk": bhk,
      "bath": bathrooms,
      "location": location,
      "area": area
    };
  
    $.post("/predict_home_price", {
        dat: JSON.stringify(data)
    }, (data, status) => {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    
    url = "http://127.0.0.1:5000/get_location_names";
    $.get(url, function(data, status) {
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            for(var i in locations) {
                var option = document.createElement("option");
                option.text = locations[i].substring(9);
                uiLocations.add(option)
            }
        }
    });
  }
  
  window.onload = onPageLoad;
  