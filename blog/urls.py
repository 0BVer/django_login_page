from django.urls import path
from blog import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.blog, name='blog'),
]
