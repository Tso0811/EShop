# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')  # 這裡加上 email 欄位

admin.site.unregister(User)  # 先取消註冊原本的
admin.site.register(User, UserAdmin)  # 用你自訂的顯示方式註冊
