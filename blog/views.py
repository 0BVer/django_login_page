from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Users
from .forms import LoginForm, RegisterForm


# Create your views here.

# 로그인
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Users.objects.get(username=username)
            if user.password == password:
                return redirect('/blog/')
            return render(request, 'login.html', {'error_message': "id pw not correct"})
        return render(request, 'login.html', {'error_message': "error"})


# 회원가입
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password == password_confirm:
                try:
                    user = Users.objects.all()
                    user.create(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'])
                    return redirect('/blog/login/')
                except:
                    return render(request, 'register.html',
                                  {'form': form, 'error_message': "change username."})
            else:
                return render(request, 'register.html',
                              {'form': form, 'error_message': "PW and PW confirm isn't same."})
    else:
        return render(request, 'register.html', {'error_message': "a"})
    return render(request, 'register.html', {'error_message': "error not allowed"})


# 블로그
def blog(request):
    if request.method == 'GET':
        return render(request, 'blog.html', {'users': Users.objects.all(), 'error_message': ""})

# 로그아웃
