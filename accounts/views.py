from django import forms
from accounts.models import Product
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

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

def customer(request,id_customer):
    customer = Customer.objects.get(id=id_customer)
    customerOrders = customer.order_set.all()
    totalOrders = customerOrders.count()

    orderFilter = OrderFilter(request.GET, queryset= customerOrders)
    customerOrders = orderFilter.qs

    context = {'customer': customer,
                'totalOrders': totalOrders,
                'customerOrders': customerOrders,
                'orderFilter': orderFilter,
              }
    return render(request, 'accounts/customer.html', context)


def createOrder(request, id_customer):
    customer = Customer.objects.get(id = id_customer)
    form = OrderForm(initial={'customer': customer})
    context = {'form': form}

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    return render(request, 'accounts/orderForm.html',context )





def editOrder(request,id_order):
    order = Order.objects.get(id = id_order)
    form = OrderForm(instance= order)

    context = {'form': form}

    if request.method == "POST":
        form = OrderForm(request.POST, instance= order)
        
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'accounts/orderForm.html', context )


def deleteOrder(request, id_order):
    order = Order.objects.get(id = id_order)
    context = {'item': order}

    if request.method == "POST":
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html', context)