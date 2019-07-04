var submit = document.getElementById("form");
submit.onclick = function(){
    var address = document.getElementById("street1_id").value;
    document.getElementById("outputAddress").innerText = address;
    alert("outputAddress")
}