var link = document.querySelector('link[rel="import"]');
link.addEventListener('load', function(e) {
  var importedDoc = link.import;

});

//On Submit click run this function from profile
function search() {
    var address = document.getElementById("street1_id").value;
    window.localStorage.setItem("street1_id",address);
    console.log(localStorage); //Checking
    document.getElementById("demo").innerHTML= address;
}

//On gallon field Click run this function from fuelquote
function delivered(){
    var delivery = localStorage.getItem('street1_id').value;
    document.getElementById("demo").innerHTML= delivery;
    console.log(delivery);
}

