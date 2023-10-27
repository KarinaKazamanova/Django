from typing import Literal
from django.utils import timezone
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    registration_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.name} {self.email} {self.adress} {self.phone_number}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='myapp/', default='myapp/no_image.png')
    def __str__(self):
        return "\n".join([f"Наименование: {self.name}",
                          f"Описание: {self.description}",
                          f"Цена: {self.price}",
                          f"Количество на складе: {self.quantity}"])
               
                

 
 
    
   
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    date_ordered = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    # def __str__(self):
    #     user = User.objects.filter(pk=self.customer.id).first()
        
    #     return (f'Заказчик: {user.name}\n{self.products}\n' + "\n" + f'Стоимость заказа: {self.total_price}')
    
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=0)  