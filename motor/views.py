from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"Rental Mobil Page | R2M",
        'heading':"Halaman Rental Motor",
        'subheading':"Rental motor-motor terbaik dan terlengkap!"
    }
    return render(request, 'motor/index.html',context)