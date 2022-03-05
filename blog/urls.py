from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
