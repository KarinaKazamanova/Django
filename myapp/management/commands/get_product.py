from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product


class Command(BaseCommand):
    help = 'Получение данных о продукте по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id продукта')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        prod = Product.objects.filter(pk=pk).first()
        if prod is not None:
            return prod
        return f'Такого товара на складе нет'
        
    
    
    
