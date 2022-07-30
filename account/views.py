from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('core:home'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'account/login.html')