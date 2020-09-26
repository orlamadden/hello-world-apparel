from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from profiles.models import UserProfile
from checkout.models import Order
from .models import Product, Category, Review

from .forms import ProductForm, ReviewForm

def all_products(request):
    """ 
    A view to show all products, 
    including sorting and search queries 
    """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'searchq' in request.GET:
            query = request.GET['searchq']
            if not query:
                messages.error(request, "Oops! You didn't enter anything in the search bar.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual
    products and information 
    """

    product = get_object_or_404(Product, pk=product_id)
    review_form = None
    reviews = Review.objects.filter(product=product_id)
    review = None

    if request.user.is_authenticated:
        profile = request.user.userprofile
        user_orders = Order.objects.filter(user_profile=profile)
        user_purchased = False
        for order in user_orders:
            for item in order.lineitems.all():
                if item.product.id == product.id:
                    user_purchased = True
                    break

        if user_purchased:
            review = Review.objects.filter(user=request.user, product=product_id)
            if review:
                review_form = None
            else:
                review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review': review,
        'page_title': product.name,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def add_review(request, product_id):
    """
    View to handle the POST of reviews from a specific user
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=product)

        form_data = {
            'comment': request.POST['comment'],
            'rating': request.POST['rating']
            }

        review_form = ReviewForm(form_data)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, f'Thank you for posting a review for {product.name}.')
        else:
            messages.error(request, f'Sorry we were unable to post your review for {product.name}, please try again')
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        review_form = ReviewForm(instance=user)

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
    }
    return render(request, 'products/product_detail.html', context)


def edit_review(request, product_id):
    """
    View to edit a current review that the user has placed on a product
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(Review, user=request.user, product=product_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=user)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, f'We have updated your review for {product.name}.')
            return redirect(reverse('product_detail', args=[product_id,]))
        else:
            messages.error(request, f'Sorry we were unable to update your review for {product.name}, please try again.')
    else:
        review_form = ReviewForm(instance=user)

    template = 'products/edit_review.html'
    context = {
        'product': product,
        'review_form': review_form,
    }
    return render(request, template, context)


def delete_review(request, product_id):
    """
    Give the user the ability to delete their review
    """
    review = get_object_or_404(Review, user=request.user, product=product_id)
    review.delete()
    messages.success(request, 'Your review has been deleted.')
    return redirect(reverse('product_detail', args=(product_id,)))