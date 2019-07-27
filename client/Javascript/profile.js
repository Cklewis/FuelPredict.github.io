"use strict";

//On Submit click run this function from profile
function store() {
    var address = document.getElementById("street1_id").value;
    window.localStorage.setItem("street1_id", address);
    console.log(localStorage); //Checking
}
