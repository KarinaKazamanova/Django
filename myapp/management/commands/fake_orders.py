import random
from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order, Product, User
from werkzeug.security import generate_password_hash
from django.shortcuts import get_list_or_404


class Command(BaseCommand):
    help = "Create fake orders"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых заказов')
        
        
        
        
    def handle(self, *args, **kwargs):
        for i in range(1, kwargs.get('number')):
            user = User.objects.filter(pk=i).first()
            prods = []
            total_price = 0
            for j in range(1, random.randint(3,8)):
                prod = Product.objects.filter(pk=j).first()
                prods.append(prod)
                total_price += prod.price
            order = Order(customer=user,
                          
                          total_price=total_price)
            order.save()
            order.products.set(prods)
            order.save()
            