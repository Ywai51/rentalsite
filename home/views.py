from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"R2M | Rental Mobil-Motor",
        'heading':"Selamat datang user!",
        'subheading':"Baru pertama kali kemari? silahkan daftar disini. Atau login jika sudah mempunyai akun."
    }
    return render(request, 'home/index.html',context)

def snkIndex(request):
    context = {
        'title':"SnK Page | R2M",
        'heading':"Syarat dan Ketentuan Layanan",
        'subheading':"Mohon dibaca dengan seksama ketentuan menyewa menggunakan website ini."
    }
    return render(request, 'home/snkIndex.html',context)