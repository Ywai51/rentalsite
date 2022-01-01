from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from akun.forms import FormAkun
from .models import NewAkun
from booking.models import bookMobil,bookMotor


def index(request):
    #cek user login/belum
    if request.user.is_authenticated:
        email = request.user.email
        akun = NewAkun.objects.get(email=email)
        pMobil = None
        pMotor = None

        if request.method == "POST":
            if request.POST['modalBtn'] == "yes":
                logout(request)
                return redirect('home:index')
            if request.POST['modalBtn'] == "ubahnomor":
                nobaru = request.POST['nobaru']
                akun.no_hp = nobaru
                akun.save()
                return redirect('akun:index')
                
        if  bookMobil.objects.filter(id_penyewa_mbl=akun).exists():
            pMobil =  bookMobil.objects.filter(id_penyewa_mbl=akun)
        if  bookMotor.objects.filter(id_penyewa_mtr=akun).exists():
            pMotor =  bookMotor.objects.filter(id_penyewa_mtr=akun)

        context = {
            'title':"Akun | R2M",
            'heading':"Hallo ",
            'subheading':"Ini adalah halaman akun anda",
            'akun' : akun,
            'pesananMbl' : pMobil,
            'pesananMtr' : pMotor
        }
        return render(request, 'akun/index.html',context)
    else:
        return redirect('akun:login')
    
def loginView(request):
    error_list = None
    form = FormAkun()
    if request.method == 'POST':
        if request.POST.get('submit') == 'daftar':
            account_form = FormAkun(request.POST)
            if account_form.is_valid():
                account_form.save()
                messages.success(request, "SELAMAT! Anda Berhasil Mendaftar, untuk masuk ke website silahkan menuju menu Login.")
                return redirect('akun:index')
            else:
                error_list = account_form.errors

        if request.POST.get('submit') == 'masuk':
            username = request.POST['emailform']
            password = request.POST['pwform']
            #cek ada user ini 
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request, "Berhasil login!")
                return redirect('akun:index')
            else:
                return redirect('akun:index')

    context = {
        'title':"Akun login | R2M",
        'heading':"Anda Belum Masuk Website!",
        'subheading':"Silahkan Masuk / Mendaftar dibawah.",
        'akunform': form,
        'error': error_list
    }
    
    return render(request, 'akun/login.html',context)