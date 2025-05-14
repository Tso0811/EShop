# orders model.py
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

# Create your models here.

class Orders(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
