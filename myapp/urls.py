from django.urls import path, include
from myapp import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('about/my_photo/', views.my_photo, name='photo'),
    path('customer_orders/<int:customer_id>/<int:days>', customer_orders, name='customer_orders'),
    path('customer/<int:customer_id>', customer, name='customer'),
    path('products/', views.products,name='products'),
    path('add_product/', views.add_product,name='add_product'),
    path('update_product/', views.update_product,name='update_product'),
    
]