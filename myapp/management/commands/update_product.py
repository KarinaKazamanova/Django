from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product
from werkzeug.security import generate_password_hash


class Command(BaseCommand):
    help = 'Обновление данных товара по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id товара')
        parser.add_argument('name', type=str, help='Название товара')
        parser.add_argument('price', type=float, help='Цена товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('quantity', type=int, help='Количество товара')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        price = kwargs.get('price')
        description = kwargs.get('description')
        quantity = kwargs.get('quantity')
   
        
        prod = Product.objects.filter(pk=pk).first()
        if prod is not None:
            if name:
                prod.name = name
            if price:
                prod.price = price
            if description:
                prod.description = description
            if quantity:
                prod.quantity = quantity
        prod.save()
        self.stdout.write(f'{prod}')
        
        
    
    
    
