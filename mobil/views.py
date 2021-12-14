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

def aboutMbl(request, slugInput):
    mbl = mobil.objects.get(slug=slugInput)
    context = {
        'title':"Detail Mobil | R2M",
        'heading' : " Halaman Detail Mobil ",
        'subheading' : 'Perhatikan Detail Mobil Yang akan disewa di halaman ini.',
        'mobil' : mbl,
        'harga' : format(mbl.harga_mbl, ',')
        #'test_group' : Group.objects.get(name='Paus'),
        #'user_group' : request.user.groups.all()
    }
    return render(request, 'mobil/aboutMobil.html',context)
 