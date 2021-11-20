from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"R2M | Rental Mobil-Motor",

    }
    return render(request, 'home/index.html',context)