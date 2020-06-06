$(document).ready(function() {
	/* Finds all the inputfields of the account signup form
     & adds proper Bootstrap class styling
     code is based on the following: https://stackoverflow.com/a/41909370 */

	$('#auth-form').find(':input').each(function(index, element) {
		$(element).addClass('form-control');
	});

	// show alerts with animation & hide them after showing.
	$('.alert').first().hide().slideDown(500).delay(4000).slideUp(500, function() {
		$(this).remove();
	});
});
