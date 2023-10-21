import datetime
import logging
import pathlib

from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from .models import Order, User,OrderProduct, Product
from django.utils import timezone
from .forms import *
from django.core.files.storage import FileSystemStorage


# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    # with open ('myapp\\templates\index_alternative.html', 'r', encoding='utf-8') as file:
    #     html = file.read()
    # return HttpResponse(html)
    # return render(request, 'index.html')
    return TemplateResponse(request, 'index.html').render()
    

def about(request):
    logger.info('About me page accessed')
    # return HttpResponse('templates\about.html')
    return render(request, 'about.html')

def my_photo(request):
    return (request, 'my_photo.jpg')


def customer_orders(request, customer_id, days):
    delta = datetime.timedelta(days=days)
    filter_day = datetime.datetime.now() - delta
    user = User.objects.filter(pk=customer_id).first()
    orders = Order.objects.filter(customer=customer_id).filter(date_ordered__gte = filter_day)
    products = []
    for order in orders:
        orderproduct = OrderProduct.objects.filter(order=order).all()
        for item in orderproduct:
            products.append(str(item.product.name))
    return render(request, 
                  'list_of_ordered_prods.html', 
                  {'list_of_prods':set(products), 
                   'user': user.name,
                   })



def customer(request, customer_id):
    result = get_list_or_404(User, pk=customer_id)
    return HttpResponse(result) 

def products(request):
    result = Product.objects.all()
    description = 'Товары на складе'
    return render(request, 
                  'list_of_ordered_prods.html', 
                  {'list':result, 
                   'description': description,
                   })
    
def add_product(request):
    desc = 'Заполните форму для загрузки нового товара'
    btn = 'Создать'
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = float(form.cleaned_data['price'])
            description = form.cleaned_data['description']
            quantity = int(form.cleaned_data['quantity'])
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            prod = Product(name=name,
                           price=price,
                           description=description,
                           quantity=quantity,
                           image=image)
            prod.save()
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form,
                                  'description': desc,
                                  'button': btn,
                                })
    
def product_not_found(request):
    return render(request, 'product_not_found.html')
    
    
def update_product(request):
    desc = 'Заполните форму для обновления данных о товаре'
    btn = 'Обновить'
    if request.method == "POST":
        form = UpdateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_id = form.cleaned_data['id']
            product = Product.objects.filter(pk=product_id).first()
            if product:
                if form.cleaned_data['name']:
                    product.name = form.cleaned_data['name']
                if form.cleaned_data['price']:
                    product.price = float(form.cleaned_data['price'])
                if form.cleaned_data['description']:
                    product.description = form.cleaned_data['description']
                if form.cleaned_data['quantity']:
                    product.quantity = form.cleaned_data['quantity']
                if form.cleaned_data['image']:
                    image = form.cleaned_data['image']
                    fs = FileSystemStorage()
                    fs.save(image.name, image)
                    product.image = image
                product.save()
            else:
                return product_not_found(request)
    else:
        form = UpdateProductForm()
    return render(request, 'form.html', {'form': form,
                                  'description': desc,
                                  'button': btn,
                                })