import random
from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Createnew user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых пользователей')
        
        
        
        
    def handle(self, *args, **kwargs):
        for i in range(kwargs.get('number')):
            user = Product(name=f'name{i}', 
                        price=f'{random.choice([i for i in range (100)])}',
                        description=f'desc of prod{i}',
                        quantity=f'{i*random.randint(0, 10)}',
                        )
            user.save()
        