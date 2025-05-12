#cart app url
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('' , views.cart_view , name='cart_view'),
    path('add/', views.add_to_cart, name='add'),
    path('update/' , views.update_cart , name='update'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove'),
    path('clear/', views.clear_cart, name='clear')
]
