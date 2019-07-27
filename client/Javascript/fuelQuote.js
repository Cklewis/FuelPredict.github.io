//On gallon & date field click, call function
function delivered(){
    var x= document.getElementById("delivery_id")
    x.setAttribute("type","text");
    x.setAttribute("value",localStorage.getItem('street1_id'))
    var delivery = localStorage.getItem('street1_id').value;
} 
