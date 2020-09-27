from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ 
    renders homepage view and
    featured listings
    """
    
    featured_products = Product.objects.filter(featured=True).order_by('?')[:6]

    context = {
        'featured_listings': featured_products,
    }

    return render(request, 'home/index.html', context)