$(document).ready(function(){
	$('img').hover(function() {
		$(this).attr('src', 'dog2.png');
	}, function() {
		$(this).attr('src', 'dog.png');
	});
});
