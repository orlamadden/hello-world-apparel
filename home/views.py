from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ homepage view """
    
    featured_products = Product.objects.filter(featured=True).order_by('?')[:6]

    context = {
        'featured_listings': featured_products,
    }

    return render(request, 'home/index.html', context)