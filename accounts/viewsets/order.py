from django import forms
from django.shortcuts import render, redirect
from accounts.models import Customer, Order
from ..forms import OrderForm
from django.contrib.auth.decorators import login_required
from ..decorators import allowed_users



#=================================================== Create Order ===================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, id_customer):
    customer = Customer.objects.get(id = id_customer)
    form = OrderForm(initial={'customer': customer})
    context = {'form': form}

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    return render(request, 'accounts/forms/orderForm.html',context )



#=================================================== Edit Order ===================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editOrder(request,id_order):
    order = Order.objects.get(id = id_order)
    form = OrderForm(instance= order)

    context = {'form': form}

    if request.method == "POST":
        form = OrderForm(request.POST, instance= order)
        
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'accounts/forms/orderForm.html', context )


#=================================================== Delete Order===================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, id_order):
    order = Order.objects.get(id = id_order)
    context = {'item': order}

    if request.method == "POST":
        order.delete()
        return redirect('/')

    return render(request, 'accounts/components/delete.html', context)