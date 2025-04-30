#products app url
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index_view , name='index_view'),
    path('products/<int:id>/' , views.products_detail_view , name='products_detail_view'),
]
