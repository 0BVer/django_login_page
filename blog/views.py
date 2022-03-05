from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Users
from .forms import LoginForm, RegisterForm


# Create your views here.

# 로그인
def loginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            user = authenticate(username='q', password='q')
            print(user)
            if user is not None:
                print(1)
                login(request, user)
                return redirect('blog')
            return render(request, 'login.html', {'form': form, 'error_message': "id pw not correct"})
        return render(request, 'login.html', {'form': form, 'error_message': "error"})


# 회원가입
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            print(password_confirm)
            print(password)
            if password == password_confirm:
                print(2)
                # try:
                user = Users.objects.all()
                user.create(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            email=form.cleaned_data['email'])

                return redirect('login')
                # except:
                #     return render(request, 'register.html',
                #                   {'form': form, 'error_message': "change username."})
            else:
                return render(request, 'register.html',
                              {'form': form, 'error_message': "PW and PW confirm isn't same."})
    else:
        return render(request, 'register.html', {'error_message': "a"})
    return render(request, 'register.html', {'error_message': "error not allowed"})


# 블로그
@login_required
def blog(request):
    if request.method == 'GET':
        return render(request, 'blog.html', {'users': Users.objects.all(), 'error_message': ""})


# 로그아웃
def logout(request):
    if request.method == 'GET':
        return render(request, 'login.html')
