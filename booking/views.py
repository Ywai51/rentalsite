from django.contrib import messages
from django.shortcuts import render, redirect
from mobil.models import mobil as mblDB
from motor.models import motor as mtrDB
from akun.models import NewAkun
from .models import bookMobil, bookMotor
import datetime

# Create your views here.
def mblBooking(request, claimInput):
    if request.user.is_staff:
        messages.warning(request, 'Silahkan gunakan akun penyewa untuk menyewa! (admin dilarang menyewa)')
        return redirect('akun:index')
    if request.user.is_authenticated is False:
        messages.warning(request, 'Silahkan mendaftar terlebih dahulu untuk menyewa!')
        return redirect('akun:index')

    current_user = request.user
    user = NewAkun.objects.get(id = current_user.id)
    mobil = mblDB.objects.get(slug=claimInput)
    total_byr = int(mobil.harga_mbl/100*25) #DP dari harga /hari sebanyak 25%
    if request.method == 'POST':
        tgl     = request.POST['tgl_sewa']
        lama    = request.POST['lama_sewa']
        nohp    = request.POST['no_hp']
        bank    = request.POST['nama_bank']
        anBank  = request.POST['atas_nama_bank']
        note    = request.POST['message']
        
        if bookMobil.objects.filter(id_mobil = mobil, tgl_booking_mbl = tgl).exists():
            messages.error(request, "Mobil ini telah dibooking pada tanggal yang dipilih, Mohon ganti tanggal atau memesan mobil yang lain. Terimakasih!")

        else:
            inputSlug = claimInput
            bookMobil.objects.create(
                id_mobil = mobil,
                id_penyewa_mbl = user, 
                tgl_booking_mbl = tgl,
                waktu_booking_mbl = lama,
                no_alternatif_mbl = nohp,
                total_sewa_mbl = mobil.harga_mbl,
                nama_bank_mbl = bank,
                atas_nama_mbl = anBank,
                note_mbl    = note
                )
            return pembayaran(request, pesananInput=inputSlug)

    context = {
        'title':"Booking Mobil | R2M",
        'heading':"Halaman Booking Mobil",
        'subheading':"Silahkan isi data dibawah untuk keperluan booking",
        'totalBayar': total_byr,
        'tglSekarang': str(datetime.datetime.now().date() + datetime.timedelta(days=1)) 

    }
    return render(request, 'booking/indexMobil.html',context)

def mtrBooking(request, claimInput):
    if request.user.is_staff:
        messages.warning(request, 'Silahkan gunakan akun penyewa untuk menyewa! (admin dilarang menyewa)')
        return redirect('akun:index')
    if request.user.is_authenticated is False:
        messages.warning(request, 'Silahkan mendaftar terlebih dahulu untuk menyewa!')
        return redirect('akun:index')

    current_user = request.user
    user = NewAkun.objects.get(id = current_user.id)
    motor = mtrDB.objects.get(slug=claimInput)
    total_byr = int(motor.harga_mtr/100*25) #DP dari harga /hari sebanyak 25%
    if request.method == 'POST':
        tgl     = request.POST['tgl_sewa']
        lama    = request.POST['lama_sewa']
        nohp    = request.POST['no_hp']
        bank    = request.POST['nama_bank']
        anBank  = request.POST['atas_nama_bank']
        note    = request.POST['message']

        if bookMotor.objects.filter(id_motor = motor, tgl_booking_mtr = tgl).exists():
            messages.error(request, "Motor ini telah dibooking pada tanggal yang dipilih, Mohon ganti tanggal atau memesan motor yang lain.  Terimakasih!")

        else:
            inputSlug = claimInput
            bookMotor.objects.create(
                id_motor = motor,
                id_penyewa_mtr = user, 
                tgl_booking_mtr = tgl,
                waktu_booking_mtr = lama,
                no_alternatif_mtr = nohp,
                total_sewa_mtr = motor.harga_mtr,
                nama_bank_mtr = bank,
                atas_nama_mtr = anBank,
                note_mtr    = note
                )
            return pembayaran(request, pesananInput=inputSlug)
    context = {
        'title':"Booking Motor | R2M",
        'heading':"Halaman Booking Motor",
        'subheading':"Silahkan isi data dibawah untuk keperluan booking",
        'totalBayar': total_byr,
        'tglSekarang': str(datetime.datetime.now().date() + datetime.timedelta(days=1)) 
    }
    return render(request, 'booking/indexMotor.html',context)

def pembayaran(request, pesananInput):
    if mblDB.objects.filter(slug = pesananInput).exists():
        mobil = mblDB.objects.get(slug=pesananInput)
        total_byr = int(mobil.harga_mbl/100*25)
    else:
        motor = mtrDB.objects.get(slug=pesananInput)
        total_byr = int(motor.harga_mtr/100*25)

    context = {
        'title':"Booking Motor | R2M",
        'heading':"Tata Cara Pembayaran",
        'totalBayar': total_byr
    }
    return render(request, 'booking/pembayaran.html',context)