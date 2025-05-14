from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem

@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, products=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            item.subtotal = item.products.price * item.quantity

 
        total_price = sum(item.subtotal for item in cart_items)

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })
    else:
        return redirect('products:products_view')
    
    
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.products.price * item.quantity for item in cart_items)

    for item in cart_items:
        item.subtotal = item.products.price * item.quantity #使用動態語言的特性新增屬性

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, products=product)

        cart_item.quantity = new_quantity
        cart_item.save()

        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.subtotal = item.products.price * item.quantity

        total_price = sum(item.subtotal for item in cart_items)

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })
    return redirect('cart:cart_view')
@login_required
def remove_from_cart(request , product_id ):
    if request.method == 'GET':
        cart = Cart.objects.get(user=request.user)  # 確保查詢的是當前用戶的購物車

        # 查找並確保這個商品是屬於當前用戶的購物車
        cart_item = get_object_or_404(CartItem, cart=cart, id=product_id)

        # 刪除這個購物車項目
        cart_item.delete()

        # 重新整理購物車資料並顯示
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.products.price * item.quantity for item in cart_items)

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })
    return redirect('cart:cart_view')
@login_required
def clear_cart(request):
    if request.method == 'GET':
        cart = get_object_or_404(Cart , user=request.user)
        CartItem.objects.filter(cart=cart).delete()
    return redirect('cart:cart_view')