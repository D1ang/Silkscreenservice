/* 
Replace the "Currently" artwork update field placeholder.
As standard Crispy-forms file field is not repsonsive on smaller screens
The placeholder text overflows the field, this will fix that problem
*/
$(document).ready(function() {
	let currentArtworkLink = document.getElementById('div_id_artwork').getElementsByClassName('d-flex')[0];
	const replaceArtworkLink = '<span><i class="fas fa-file-alt"></i> Artwork uploaded</span>';

	currentArtworkLink.innerHTML = replaceArtworkLink;
});
