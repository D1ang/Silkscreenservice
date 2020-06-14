/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment-charges

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

let style = {
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
		color: '#ff0000',
		iconColor: '#ff0000'
	}
};

let card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
	let errorDiv = document.getElementById('card-errors');
	if (event.error) {
		let html = `
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
let form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  
  stripe.createToken(card).then(function(result) {
    if (result.error) {
      let errorElement = document.getElementById('card-errors');
      let html = `
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
  let form = document.getElementById('payment-form');
  let hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);
  form.submit();
}

