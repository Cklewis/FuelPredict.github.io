//Doesn't really work
submit.onclick = function(){
    var address = document.getElementById("street1_id").value;
    document.getElementById("outputAddress").innerText = address;
    alert("outputAddress");
}


function search(ele) {
    if(event.key === 'Enter') {
        alert(ele.value);        
    }
}