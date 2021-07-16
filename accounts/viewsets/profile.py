from django import forms
from django.shortcuts import redirect, render
from accounts.models import Customer
from accounts.forms import customerForm
from ..filters import OrderFilter
from django.contrib.auth.decorators import login_required
from ..decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profile(request):
    customer = request.user.customer
    form  = customerForm(instance = customer)
    context = {'form': form }

    if request.method == "POST":
        form = customerForm(request.POST, request.FILES, instance= customer)
        if form.is_valid():
            form.save()
            return redirect('profile')
            

    return render(request,'accounts/pages/profile.html', context)