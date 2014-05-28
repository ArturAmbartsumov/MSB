$('.projectsGallerie_project').hover(showText, hideText);

function showText(){
	textDiv = $('.projectsGallerie_project_text', this).slideDown('fast');
}

function hideText(){
  textDiv = $('.projectsGallerie_project_text', this).slideUp('fast');
}

/*------------------------------------------Progect-Carousell-Many-Items------------------------

$('.carousel[data-type="multi"] .item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));
  
  for (var i=0;i<2;i++) {
    next=next.next();
    if (!next.length) {
    	next = $(this).siblings(':first');
  	}
    
    next.children(':first-child').clone().appendTo($(this));
  }
});*/


