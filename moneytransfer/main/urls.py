from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('search/', views.search, name = 'search'),
    path('add_friend/<int:pk>', views.add_f, name ='add_f'),
    path('accept/<int:pk>/<int:fr>', views.accept, name ='accept'),
    path('transfer_request/<int:pk>/<int:fr>', views.transfer_request, name ='transfer_request'),
]
