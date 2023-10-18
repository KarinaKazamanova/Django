from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product




class Command(BaseCommand):
    help = "Createnew product"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Название товара')
        parser.add_argument('price', type=float, help='Цена товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('quantity', type=int, help='Количество товара')
       
        
        
    def handle(self, *args, **kwargs):
        product = Product(name=kwargs.get('name'), 
                    price=kwargs.get('price'),
                    description=kwargs.get('description'),
                    quantity=kwargs.get('quantity'),
                   )
        product.save()
        self.stdout.write(f'{product}')