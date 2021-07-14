from django import forms
from django.shortcuts import render, redirect
from accounts.models import Customer, Order



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
