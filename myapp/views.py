import logging

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    # with open ('myapp\\templates\index_alternative.html', 'r', encoding='utf-8') as file:
    #     html = file.read()
    # return HttpResponse(html)
    return render(request, 'index.html')

def about(request):
    logger.info('About me page accessed')
    # return HttpResponse('templates\about.html')
    return render(request,  'about.html')

def my_photo(request):
    return (request, 'my_photo.jpg')