from os import name
from django.urls import path
from . import views

urlpatterns = [
        path('', views.cart, name='cart'),
        path('charge', views.charge, name='charge')
]