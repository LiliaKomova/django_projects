from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    import csv

    with open(settings.BUS_STATION_CSV) as f:
        reader = csv.DictReader(f)
        s = [row for row in reader]

        paginator = Paginator(s, 10)
        page = paginator.get_page(request.GET.get('page'))

    context = {

        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
