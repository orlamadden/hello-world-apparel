from django.shortcuts import render

# Create your views here.

def index(request):
    """ homepage view """
    return render(request, 'home/index.html')