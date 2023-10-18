from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Createnew user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Адрес электронной почты пользователя')
        parser.add_argument('number', type=str, help='Номер телефона пользователя')
        parser.add_argument('adress', type=str, help='Адрес пользователя')
        parser.add_argument('pswd', type=str, help='Пароль пользователя')
        
        
        
    def handle(self, *args, **kwargs):
        user = User(name=kwargs.get('name'), 
                    email=kwargs.get('email'),
                    phone_number=kwargs.get('number'),
                    adress=kwargs.get('adress'),
                    password=generate_password_hash(kwargs.get('pswd')))
        user.save()
        self.stdout.write(f'{user}')