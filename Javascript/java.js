/* $(function () {
    $('#datepicker').datepicker({
        format: "dd/mm/yyyy",
        autoclose: true,
        todayHighlight: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        autoclose: true,
        changeMonth: true,
        changeYear: true,
        orientation: "button"
    });
}); */

var submit = document.getElementById("submit");
submit.onclick=function(){
    var street1_id=document.getElementById("street1_id").nodeValue;
    document.getElementById("outputAddress").innerText=streed1_id;
}