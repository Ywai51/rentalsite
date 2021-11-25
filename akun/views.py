from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"Akun | R2M",
        'heading':"Hallo user",
        'subheading':"ini page akun"
    }
    return render(request, 'akun/index.html',context)