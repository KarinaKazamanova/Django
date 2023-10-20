import random
from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Createnew user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых пользователей')
        
        
        
        
    def handle(self, *args, **kwargs):
        for i in range(kwargs.get('number')):
            user = User(name=f'name{i}', 
                        email=f'email{i}@mail.com',
                        phone_number=f'{''.join(random.choices([str(i) for i in range(1,10)], k=15))}',
                        adress=f'adress{i}',
                        password=generate_password_hash(f'{random.choices(['e','w','W','1','@','&','6','m'], k=15)}'))
            user.save()
        