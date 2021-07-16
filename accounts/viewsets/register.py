from accounts.models.customer import Customer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ..forms.CreateUserForm import CreateUserForm
from django.contrib import messages
from ..decorators import unauthenticated_user
from django.contrib.auth.models import Group
import re

@unauthenticated_user
def registerPage(request):
   
    form  = CreateUserForm()
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        print('request.POST.password1:', request.POST.get('password1')) 
        #para obtener un dato directamente de request.POST usar .get('campo')    
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        passValidated = re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}', pass1)        

        if passValidated:

            if pass1 == pass2:
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
    
                    messages.success(request, 'Account was created for ' + username)

                    return redirect('login')
            else:
                messages.error(request, 'Password doesn\'t match')
        else:
            messages.error(request, 'Password is not valid')


    return render(request, 'accounts/pages/register.html', context)

