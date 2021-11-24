
$(document).ready(function(){
    // script for loading calendar jquery thingy
    $(".datetimeinput").datepicker({changeYear: true, changeMonth: true, dateFormat:'yy-mm-dd'});

    // script for pagination on list_item.html
    $('.table').paging({limit:10});
});