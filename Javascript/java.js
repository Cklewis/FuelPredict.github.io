
function search() {
    var address = document.getElementById("street1_id").value;
    localStorage.setItem("street1_id",address);
    console.log(localStorage);
    document.getElementById("delivery_id").innerHTML= address;

}
