$('.projectsGallerie_project').hover(showText, hideText);

function showText(){
	textDiv = $('.projectsGallerie_project_text', this).slideDown('fast');
}

function hideText(){
	textDiv = $('.projectsGallerie_project_text', this).slideUp('fast');
}