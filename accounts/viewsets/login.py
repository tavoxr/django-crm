from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):
    
    if request.method == "POST":
        username =  request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'accounts/pages/login.html', context)



def logoutUser(request):
    logout(request)

    return redirect('login')

