from django.shortcuts import render, redirect

# Create your views here.
def view_cart(request):
    """ A view that renders the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    print( request.session['cart'])
    return redirect(redirect_url)
