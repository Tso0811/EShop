# cart model.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Cart (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.username}的購物車")

class CartItem (models.Model):

    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    products = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.products.name} x {self.quantity}"    