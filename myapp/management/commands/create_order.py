from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order, Product




class Command(BaseCommand):
    help = "Createnew product"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('customer', type=int, help='Название товара')
        parser.add_argument('products', type=list(int), help='Цена товара')
        parser.add_argument('total_price', type=str, help='Стоимость заказа')
      
       
        
        
    def handle(self, *args, **kwargs):
        order = Order(customer=kwargs.get('customer'))
        for prod in kwargs.get('products'):
            order.products.add(prod)
            order.total_price += Product.objects.filter(pk=prod).first().price # Пока считаю, чтотовары добавляются по одному (даже если покупается несколько штук одного и того же товара
        order.save()
        self.stdout.write(f'{order}')