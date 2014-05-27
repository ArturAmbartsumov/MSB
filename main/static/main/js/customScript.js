$('.projectsGallerie_project').hover(showText, hideText);

function showText(){
	textDiv = $('.projectsGallerie_project_text', this).slideDown('fast');
}

function hideText(){
	textDiv = $('.projectsGallerie_project_text', this).slideUp('fast');
}

$(document).ready(function() {
	$('#myCarousel').carousel({
	interval: 0
	})
    
    $('#myCarousel').on('slid.bs.carousel', function() {
    	//alert("slid");
	});
    
    
});

