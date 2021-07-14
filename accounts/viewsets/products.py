from django import forms
from django.shortcuts import render
from accounts.models import Product



def products(request):

    products = Product.objects.all()
    
    
    return render(request, 'accounts/products.html', {'products': products} )