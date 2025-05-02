#accounts views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout , authenticate , login 
from django.contrib.auth.models import User

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('products:index_view')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)

        if user is not None :
            login(request , user)
            return redirect ('products:index_view')
        else :
            return render(request, 'login.html', {'error': '帳號或密碼錯誤'})
    return render (request , 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request , 'register.html' ,{'errorpass':'密碼與確認密碼不一致'})
        
        if  User.objects.filter(username=username).exists():
            return render(request , 'register.html' , {'errorname':'使用者名稱已存在'})
        if User.objects.filter(email=email).exists():
            return render(request , 'register.html' , {'errormail':'電子郵件已存在'})
        
        user = User.objects.create_user(username=username , password=password1)
        login(request , user)
        return redirect('products:index_view')
    
    return render(request, 'register.html')  

def account_view(request):
    if  request.user.is_authenticated:
        username = request.POST.get('username')
        mail = request.POST.get('mail')

        user = {
            'username':username,
            'email':mail
            }
    else :
        return redirect('accounts:login_view')
    return render(request , 'account.html' , user)
