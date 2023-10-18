import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View

# Create your views here.

logger = logging.getLogger(__name__)

class Index(View):
    def index(self, request):
        logger.info('Index page accessed')
        # with open ('myapp\\templates\index_alternative.html', 'r', encoding='utf-8') as file:
        #     html = file.read()
        # return HttpResponse(html)
        # return render(request, 'index.html')
        return TemplateResponse(request, 'index.html').render()
    

class About(View):
    def about(self, request):
        logger.info('About me page accessed')
        # return HttpResponse('templates\about.html')
        return render(request, 'about.html')

def my_photo(request):
    return (request, 'my_photo.jpg')


