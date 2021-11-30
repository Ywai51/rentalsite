from django.shortcuts import render
from .models import motor

from django.core.paginator import Paginator

from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.

def index(request):

    p = Paginator(motor.objects.all(), 2)
    page = request.GET.get('page')
    mtr = p.get_page(page)

    context = {
        'title':"Rental Mobil Page | R2M",
        'heading':"Halaman Rental Motor",
        'subheading':"Rental motor-motor terbaik dan terlengkap!",
        'mtr':mtr,
    }
    return render(request, 'motor/index.html',context)