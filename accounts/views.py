from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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

        # 학번 중복 검사
        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ 이미 가입된 학번입니다!')
            return redirect('accounts:agree')

        context = authenticate(username, password)
        if context:
            context['id'] = username
            request.session['context'] = context
            return redirect('accounts:signup')
        else:
            messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
            return redirect('accounts:agree')

    else:
        messages.error(request, '⚠️ 잘못된 접근입니다!')
        return redirect('core:home')


def signup(request):
    context = request.session.get('context')
    return render(request, 'accounts/signup.html', context)