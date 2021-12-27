from django.contrib import admin
from .models import motor

# Register your models here.
class MotorConfig(admin.ModelAdmin):
    model = motor
    search_fields   = ('plat_mtr','nama_mtr','merk_mtr','kategori_mtr','warna_mtr')
    ordering        = ('-tgl_db_mtr',)
    list_display    = ('plat_mtr','merk_mtr','nama_mtr','warna_mtr','harga_mtr','status_mtr','kategori_mtr')
    readonly_fields = ['slug']

admin.site.register(motor,MotorConfig)