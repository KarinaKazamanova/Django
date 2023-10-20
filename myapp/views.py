import logging

from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from .models import Order, User,OrderProduct

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


def customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    products = []
    for order in orders:
        orderproduct = OrderProduct.objects.filter(order=order).all()
        for item in orderproduct:
            products.append(str(item.product.name))
    return render(request, 'list_of_ordered_prods.html', {'list_of_prods':set(products), 'user': User.objects.filter(pk=customer_id).first().name})



def customer(request, customer_id):
    result = get_list_or_404(User, pk=customer_id)
    return HttpResponse(result) 