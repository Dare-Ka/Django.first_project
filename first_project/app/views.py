from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    msg = f'Текущее время: {datetime.now().strftime("%Y-%m-%d | %H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = f'Содержимое рабочей директории: {os.listdir()}'
    return HttpResponse(msg)
