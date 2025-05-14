#主專案 url
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.url')),
    path('accounts/' , include( 'accounts.url' , namespace='accounts' )),
    path('cart/' , include('cart.url' , namespace='cart')),
    path('orders/',include('orders.url' , namespace='orders'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
