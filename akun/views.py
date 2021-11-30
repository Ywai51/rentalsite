from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from akun.forms import FormAkun
from .models import NewAkun


# Create your views here.
def index(request):
    #cek user login/belum
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['logout'] == "yes":
                logout(request)
                return redirect('home:index')
        email = request.user.email
        akun = NewAkun.objects.get(email=email)
        context = {
            'title':"Akun | R2M",
            'heading':"Hallo ",
            'subheading':"ini page akun",
            'akun' : akun
        }

        return render(request, 'akun/index.html',context)
    else:
        return redirect('akun:login')
    
def loginView(request):
    form = FormAkun()
    if request.method == 'POST':
        if request.POST.get('submit') == 'daftar':
            account_form = FormAkun(request.POST)
            if account_form.is_valid():
                account_form.save()
                return redirect('home:index')
            else:
                error_list = account_form.errors.as_data()
                messages.error(request, error_list)

        if request.POST.get('submit') == 'masuk':
            username = request.POST['emailform']
            password = request.POST['pwform']
            #cek ada user ini 
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home:index')
            else:
                return redirect('akun:index')

    context = {
        'title':"Akun login | R2M",
        'heading':"Anda Belum Masuk Website!",
        'subheading':"Silahkan Masuk / Mendaftar dibawah.",
        'akunform': form
    }
    
    return render(request, 'akun/login.html',context)