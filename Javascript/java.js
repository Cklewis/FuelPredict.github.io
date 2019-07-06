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

function goBack() {
  window.history.back()
}

var firebaseConfig = {
  apiKey: "api-key",
  authDomain: "project-id.firebaseapp.com",
  databaseURL: "https://project-id.firebaseio.com",
  projectId: "project-id",
  storageBucket: "project-id.appspot.com",
  messagingSenderId: "sender-id",
  appID: "app-id",
};

firebase.initializeApp(config);

var ref = firebase.database().ref();                           
ref.on("value", function(snapshot){
  output.innerHTML = JSON.stringify(snapshot.val(), null, 2);
});

