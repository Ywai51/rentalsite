from django.shortcuts import render
from .models import mobil

from django.core.paginator import Paginator

from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.

def index(request):
    p = Paginator(mobil.objects.all(), 2)
    page = request.GET.get('page')
    mbl = p.get_page(page)

    context = {
        'title':"Rental Mobil Page | R2M",
        'heading':"Halaman Rental Mobil",
        'subheading':"Rental Mobil dari yang terbaik sampai yang termewah!",
        'mbl' : mbl,
    }
    return render(request, 'mobil/index.html',context)