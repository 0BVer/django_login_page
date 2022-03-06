from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Users
from .forms import LoginForm, RegisterForm

# Create your views here.
loginTemp = 'sign-in/index.html'
blogTemp = 'blog.index.html'


# 로그인
def loginView(request):
    if request.method == 'GET':
        return render(request, loginTemp)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog')
            return render(request, 'login.html', {'form': form, 'error_message': "id pw not correct"})
        return render(request, 'login.html', {'form': form, 'error_message': "error"})


# 회원가입
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password == password_confirm:
                try:
                    users = Users.objects.all()
                    user = users.create(username=form.cleaned_data['username'],
                                        email=form.cleaned_data['email'])
                    user.set_password(password)
                    user.save()
                    return redirect('login')
                except:
                    return render(request, 'register.html',
                                  {'form': form, 'error_message': "change username."})
            else:
                return render(request, 'register.html',
                              {'form': form, 'error_message': "PW and PW confirm isn't same."})
    else:
        return render(request, 'register.html', {'error_message': ""})
    return render(request, 'register.html', {'error_message': "error not allowed"})


# 블로그
@login_required
def blogView(request):
    if request.method == 'GET':
        return render(request, 'blog.html', {'users': Users.objects.all(), 'error_message': ""})


# 로그아웃
def logoutView(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'login.html')
