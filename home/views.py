from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"R2M | Rental Mobil-Motor",
        'heading':"Welcome user!!",
        'subheading':"Silahkan pilih kendaraan yang akan disewa "
    }
    return render(request, 'home/index.html',context)