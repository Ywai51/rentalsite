from django.contrib import admin
from booking.models import bookMobil, bookMotor

# Register your models here.
class bookMobilConfig(admin.ModelAdmin):
    model = bookMobil
    search_fields   = ('id_mobil__nama_mbl','id_mobil__plat_mbl','id_penyewa_mbl__nama','id_penyewa_mbl__email','no_alternatif_mbl','atas_nama_mbl')
    ordering        = ('-tgl_reservasi_mbl',)
    list_display    = ('id_mobil','id_penyewa_mbl','tgl_booking_mbl','total_sewa_mbl','status_sewa_mbl','note_mbl')

class bookMotorConfig(admin.ModelAdmin):
    model = bookMotor
    search_fields   = ('id_motor__nama_mtr','id_motor__plat_mtr','id_penyewa_mtr__nama','id_penyewa_mtr__email','no_alternatif_mtr','atas_nama_mtr')
    ordering        = ('-tgl_reservasi_mtr',)
    list_display    = ('id_motor','id_penyewa_mtr','tgl_booking_mtr','total_sewa_mtr','status_sewa_mtr','note_mtr')

admin.site.register(bookMobil, bookMobilConfig)
admin.site.register(bookMotor, bookMotorConfig)
