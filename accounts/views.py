from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.ecampus import ecampus
from accounts.forms import UserForm
from core.models import Information
from accounts.models import Profile


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = ecampus(username, password)

        if user:
            auth_login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('core:home'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def agree(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # 학번 중복 검사
        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ 이미 가입된 학번입니다!')
            return redirect('accounts:agree')

        context = ecampus(username, password)
        if context:
            context['id'] = username
            request.session['context'] = context
            return redirect('accounts:signup')
        else:
            messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
            return redirect('accounts:agree')

    else:
        return render(request, 'accounts/agree.html')


def signup(request):
    context = request.session.get('context')

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            information = Information.objects.filter(year=context['id'][:4], department=context['department']).first()

            if information:     # 지원하는 학과와 학번인지 확인
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                Profile.objects.create(user=user, information=information, name=context['name'])
                auth_login(request, user)  # 로그인
            else:
                messages.error(request, '⚠️ 서비스에서 지원하지 않는 학과와 학번 입니다.')
            return redirect('core:home')
        else:
            messages.error(request, '⚠️ 비밀번호가 동일하지 않습니다.')
            return redirect('accounts:signup')

    else:
        form = UserForm()
    context['form'] = form
    return render(request, 'accounts/signup.html', context)