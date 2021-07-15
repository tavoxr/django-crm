from django.shortcuts import render, redirect


def userPage(request):


    context = {}
    return render(request,'accounts/pages/user.html',context)