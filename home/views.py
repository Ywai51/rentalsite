from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"R2M | Rental Mobil-Motor",
        'heading':"Selamat datang user!",
        'subheading':"Baru pertama kali kemari? silahkan daftar disini. Atau login jika sudah mempunyai akun."
    }
    return render(request, 'home/index.html',context)