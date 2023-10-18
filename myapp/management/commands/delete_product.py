from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product


class Command(BaseCommand):
    help = 'Удаление товара по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id товара')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        prod = Product.objects.filter(pk=pk).first()
        if prod:
            prod.delete()
        return f'Такого нет'
        
    
    
    
