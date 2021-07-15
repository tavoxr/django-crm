from django.shortcuts import render, redirect
from ..models import Order
from django.contrib.auth.decorators import login_required
from ..decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    customerOrders = request.user.customer.order_set.all()
    ordersTotal = customerOrders.count()
    ordersDelivered = customerOrders.filter(status = 'Delivered').count()
    ordersPending =  customerOrders.filter(status = 'Pending').count()

    context = {'customerOrders': customerOrders,
                'ordersTotal': ordersTotal,
                'ordersDelivered':   ordersDelivered,
                'ordersPending': ordersPending,
              }
    return render(request,'accounts/pages/user.html',context)