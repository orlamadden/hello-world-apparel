from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your shoppping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'sk_test_51HCJuFDggnVOYdNoQZtTTbetEcYTTnIBEmXOH7ysY4o8zuSd0CDq0SRYcizmiRbFAiXsIwKY1FZK2L6XThR4n0Cz00qW7M992o',
        'client_secret': 'test_client',
    }

    return render(request, template, context)


def calc_subtotal(price, quantity):
    return price * quantity