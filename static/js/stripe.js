/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment-charges

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
	base: {
		color: '#32325d',
		fontFamily: '"Poppins", sans-serif',
		fontSmoothing: 'antialiased',
		fontSize: '17px',
		'::placeholder': {
			color: '#aab7c4'
		}
	},
	invalid: {
		color: '#fa755a',
		iconColor: '#fa755a'
	}
};

var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
	var errorDiv = document.getElementById('card-errors');
	if (event.error) {
		var html = `
      <div class="stripe-icon my-2 pl-1">
        <i class = "fas fa-times"></i> ${event.error.message}
      </div>
    `;
		$(errorDiv).html(html);
	} else {
		errorDiv.textContent = '';
	}
});

// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  
  stripe.createToken(card).then(function(result) {
    if (result.error) {
      var errorElement = document.getElementById('card-errors');
      var html = `
            <div class="stripe-icon my-2 pl-1">
              <i class = "fas fa-times"></i> ${result.error.message}
            </div>`;
      $(errorElement).html(html);
    } else {
      stripeTokenHandler(result.token);
    }
  });
});

// Send token to backend
function stripeTokenHandler(token) {
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);
  form.submit();
}

