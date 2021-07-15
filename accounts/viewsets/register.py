from accounts.models.customer import Customer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ..forms.CreateUserForm import CreateUserForm
from django.contrib import messages
from ..decorators import unauthenticated_user
from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
   
    form  = CreateUserForm()
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    return render(request, 'accounts/pages/register.html', context)

