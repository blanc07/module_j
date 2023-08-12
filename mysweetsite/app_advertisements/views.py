from django.shortcuts import render
from .models import Advertisement
from django.http import HttpResponse

# Create your views here.


def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
