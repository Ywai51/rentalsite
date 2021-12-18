from django.shortcuts import render, redirect
from .models import motor

from django.core.paginator import Paginator

from django.contrib.auth.models import Group
from django.contrib import messages


# Create your views here.

def index(request):
    kat = None
    p = Paginator(motor.objects.all(), 3)
    page = request.GET.get('page')
    mtr = p.get_page(page)

    #FILTER Jenis motor
    if request.method == "POST":
        kat = request.POST['kategori']
        return redirect('motor:kategoriMotor', slugInput=kat)
    
    context = {
        'title':"Rental Motor Page | R2M",
        'heading':"Halaman Rental Motor",
        'subheading':"Rental motor-motor terbaik dan terlengkap!",
        'mtr':mtr,
        'kategori':kat
    }
    return render(request, 'motor/index.html',context)


def kategoriMtr(request, slugInput):
    kat = slugInput

    #FILTER Jenis mobil
    if request.method == "POST":
        kat = request.POST['kategori']
        if kat == 'Semua':
            return redirect('motor:index')

        return redirect('motor:kategoriMotor', slugInput=kat)

    p = Paginator(motor.objects.filter(kategori_mtr=kat), 3)
    page = request.GET.get('page')
    mtr  = p.get_page(page)
    
    context = {
        'title':"Rental Mobil Page | R2M",
        'heading':"Halaman Rental Mobil",
        'subheading':"Rental Mobil dari yang terbaik sampai yang termewah!",
        'mtr' : mtr,
        'kategori' : kat
    }
    return render(request, 'motor/sortMotor.html',context)


def aboutMtr(request, slugInput):
    mtr = motor.objects.get(slug=slugInput)
    context = {
        'title':"Detail Motor | R2M",
        'heading' : " Halaman Detail Motor ",
        'subheading' : 'Perhatikan Detail Motor Yang akan disewa di halaman ini.',
        'motor' : mtr,
        'harga' : format(mtr.harga_mtr, ',')
    }
    return render(request, 'motor/aboutMotor.html',context)
