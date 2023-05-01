from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    from datetime import datetime

    raw = datetime.now()
    current_time = datetime.strftime(raw, '%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    import os

    roster = ' ', os.listdir()
    return HttpResponse(roster)

