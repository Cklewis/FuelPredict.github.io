function hist(){
    var x= document.getElementById("address")
    x.setAttribute("td","text");
    x.setAttribute("value",localStorage.getItem('street1_id'))
    var delivery = localStorage.getItem('street1_id').value;
} 