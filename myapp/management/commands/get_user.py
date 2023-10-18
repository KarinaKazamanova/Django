from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User


class Command(BaseCommand):
    help = 'Получение данных пользователя по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id пользователя')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            return user
        return f'Такого нет'
        
    
    
    
