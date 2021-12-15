from django.shortcuts import render
from mobil.models import mobil
from motor.models import motor
from django.db.models import Q
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

def searchView(request):
    if request.method == 'GET':
        search = request.GET.get("search")
        
        mbl = mobil.objects.all().filter(Q(nama_mbl__icontains=search) | Q(merk_mbl__icontains=search))
        mtr = motor.objects.all().filter(Q(nama_mtr__icontains=search) | Q(merk_mtr__icontains=search))

        context = {
            'title':"Search Page | R2M",
            'heading':"Halaman Pencarian",
            'subheading':"Menampilkan Hasil Pencarian untuk ",
            'listMotor': mtr,
            'listMobil': mbl,
            'value' : search
        }
        return render(request, 'home/search.html',context)
