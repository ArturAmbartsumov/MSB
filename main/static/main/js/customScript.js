//$(document).ready(function(){
//    $('#fixed-menu').hide();
//});

$('.projectsGallerie_project').hover(showText, hideText);

function showText(){
	textDiv = $('.projectsGallerie_project_text', this).slideDown('fast');
}

function hideText(){
  textDiv = $('.projectsGallerie_project_text', this).slideUp('fast');
}

/*$(window).scroll(function(){
    var windowpos = $(window).scrollTop();
    if(windowpos > 50) {
        $('#trensperent-menu').hide();
        $('#fixed-menu').show();
    } else {
        $('#fixed-menu').hide();
        $('#trensperent-menu').show();
    }
});*/


