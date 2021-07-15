from django import forms
from django.shortcuts import render
from accounts.models import Product
from django.contrib.auth.decorators import login_required
from ..decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):

    products = Product.objects.all()
    
    
    return render(request, 'accounts/pages/products.html', {'products': products} )