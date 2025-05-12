from django.contrib import admin
from .models import Cart , CartItem

# 註冊 Category 和 Product 模型
admin.site.register(Cart)
admin.site.register(CartItem)