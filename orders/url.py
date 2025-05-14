#orders url.py
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('checkout/', views.checkout_view , name='checkout_view'),
]
