from django import forms
from django.shortcuts import render
from accounts.models import Customer
from ..filters import OrderFilter


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

