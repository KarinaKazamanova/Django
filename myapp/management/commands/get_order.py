from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order


class Command(BaseCommand):
    help = 'Получение данных пользователя по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id пользователя')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            return order
        return f'Такого нет'
        
    
    
    
