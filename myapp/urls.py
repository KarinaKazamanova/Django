from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('about/my_photo/', views.my_photo, name='photo')
]