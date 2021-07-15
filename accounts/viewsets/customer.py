from django import forms
from django.shortcuts import render
from accounts.models import Customer
from ..filters import OrderFilter
from django.contrib.auth.decorators import login_required
from ..decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
              
    return render(request, 'accounts/pages/customer.html', context)

