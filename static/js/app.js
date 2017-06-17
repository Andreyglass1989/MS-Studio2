$(document).ready(function(){
    if ('.item .active' == true)(function(){
        $(".carousel-caption").fadeIn(2500)
    });


    $('.carousel').carousel({
    interval:500,
    slideSpeed : 200,
    autoHeight : false,
    })

    //$('#carousel').on('slid.bs.carousel', function () { });

});