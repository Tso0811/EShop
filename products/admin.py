from django.contrib import admin
from .models import Category, Product

# 註冊 Category 和 Product 模型
admin.site.register(Category)
admin.site.register(Product)