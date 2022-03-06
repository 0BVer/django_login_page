from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogView, name='blog'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', views.logoutView, name='logout'),
]
