from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from products.models import Product

# Create your views here.

@login_required
def checkout_view(request): 
    cart_user = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart_user)

    for item in cart_items:
        item.subtotal = item.products.price * item.quantity
        
    total_price = sum(item.products.price * item.quantity for item in cart_items)

    return render(request , 'checkout.html' , {'cart_items':cart_items , 'total_price':total_price})