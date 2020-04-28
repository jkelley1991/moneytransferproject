from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('users/', views.users , name ='users'),
    path('search/', views.search, name = 'search'),
    path('add_friend/<int:pk>', views.add_f, name ='add_f'),
    path('accept/<int:pk>', views.accept, name ='accept')
]
