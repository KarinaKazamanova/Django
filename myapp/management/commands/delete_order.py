from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order


class Command(BaseCommand):
    help = 'Удаление заказа по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id заказа')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order:
            order.delete()
        return f'Такого нет'
        
    
    
    
