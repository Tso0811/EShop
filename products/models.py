from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100 , blank=False , null=False)          #商品名
    price = models.IntegerField(blank=False , null=False)                       #商品價格(整數)
    description = models.TextField(blank=True , null=True)                      #商品說明
    image = models.ImageField(upload_to='products/' , blank=True , null=True )  #商品圖片 之後可設一個defult

    category = models.ForeignKey(Category , on_delete=models.CASCADE)           

    def __str__(self):
        return self.name