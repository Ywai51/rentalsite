from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title':"Rental Mobil Page | R2M",
        'heading':"Halaman Rental Mobil",
        'subheading':"Rental Mobil dari yang terbaik sampai yang termewah!"
    }
    return render(request, 'mobil/index.html',context)