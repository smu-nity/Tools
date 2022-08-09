from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from accounts.ecampus import authenticate


def login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username, password)

        if user:
            auth_login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('core:home'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html')

def agree(request):
    if request.method == "GET":
        return render(request, 'accounts/agree.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username, password)

        if user:
            return HttpResponseRedirect(reverse('accounts:signup'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html')



def signup(request):
    return render(request, 'accounts/signup.html')