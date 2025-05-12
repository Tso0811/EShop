#produucts views.py
from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.

def index_view(request):            #首頁(顯示熱門商品)
    products = Product.objects.order_by('id')[:4]
    return render(request , 'index.html' , {'products':products ,  'is_product_list':False})

def products_view(request):
    products = Product.objects.all()
    return render (request , 'index.html' ,{'products':products , 'is_product_list':True})

def products_detail_view(request , id): #顯示商品細節
    products = get_object_or_404(Product , pk = id)
    return render (request , 'products_detail.html' , {'product':products})

