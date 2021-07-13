from accounts.models import Product
from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    orders = Order.objects.all()
    ordersTotal = orders.count()
    ordersDelivered = Order.objects.filter(status = "Delivered").count()
    ordersPending = Order.objects.filter(status = "Pending").count()
    customers = Customer.objects.all()

    context = {'orders': orders, 
            'ordersTotal': ordersTotal, 
            'ordersDelivered': ordersDelivered, 
            'ordersPending': ordersPending,
            'customers': customers,
            }

    return render(request, 'accounts/dashboard.html', context)


def products(request):

    products = Product.objects.all()
    
    
    return render(request, 'accounts/products.html', {'products': products} )

def customer(request):
    return render(request, 'accounts/customer.html')

