from django.shortcuts import render

# Create your views here.
def view_cart(request):
    """ A view that renders the shopping cart """
    return render(request, 'cart/cart.html')