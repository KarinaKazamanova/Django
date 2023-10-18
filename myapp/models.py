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
        return f'{self.name} {self.email}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    # image = models.ImageField(upload_to='products/')
    def __str__(self):
        return f'{self.name}\n{self.description}\nЦена: {self.price}\n Количество на складе: {self.quantity}'
    
 
 
    
   
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    date_ordered = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        user = User.objects.filter(pk=self.customer).first()
        product_info = ''
        for prod in self.products:
            product_info += prod.name
        return (f'Заказчик: {user.name}\n{self.description}\n' + product_info + "\n" + f'Стоимость заказа: {self.total_price}')
    
    
class OrderProduct(models.Model):
    order =  models.ForeignKey(Order, on_delete=models.CASCADE)
    product =   models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()  