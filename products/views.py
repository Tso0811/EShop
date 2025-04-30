from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.

def index_view(request):            #首頁
    product = Product.objects.all()
    return render(request , 'index.html' , {'products':product})

def products_detail_view(request , id):
    product = get_object_or_404(Product , pk = id)
    return render (request , 'products_detail.html' , {'product':product})

