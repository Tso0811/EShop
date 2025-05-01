#products app url
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('' , views.index_view , name='index_view'),
    path('products/' , views.products_view , name='products_view'),
    path('products/<int:id>/' , views.products_detail_view , name='products_detail_view'),
]
