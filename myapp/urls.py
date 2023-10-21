from django.urls import path
from myapp import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('about/my_photo/', views.my_photo, name='photo'),
    path('customer_orders/<int:customer_id>/<int:days>', customer_orders, name='customer_orders'),
    path('customer/<int:customer_id>', customer, name='customer'),
]