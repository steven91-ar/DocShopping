from itertools import product

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})
