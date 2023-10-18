from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User
from werkzeug.security import generate_password_hash


class Command(BaseCommand):
    help = 'Обновление данных пользователя по его id'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='id пользователя')
        parser.add_argument('name', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Адрес электронной почты пользователя')
        parser.add_argument('number', type=str, help='Номер телефона пользователя')
        parser.add_argument('adress', type=str, help='Адрес пользователя')
        parser.add_argument('pswd', type=str, help='Пароль пользователя')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('number')
        adress = kwargs.get('adress')
        password =  kwargs.get('pswd')
        
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            if name:
                user.name = name
            if email:
                user.email = email
            if phone_number:
                user.phone_number = phone_number
            if adress:
                user.adress= adress
            if password:
                user.password = generate_password_hash(password)
        user.save()
        self.stdout.write(f'{user}')
        
        
    
    
    
