from django.contrib import admin
from .models import mobil

# Register your models here.
class MobilConfig(admin.ModelAdmin):
    model = mobil
    search_fields   = ('plat_mbl','nama_mbl','merk_mbl','kategori_mbl','warna_mbl')
    ordering        = ('-tgl_db_mbl',)
    list_display    = ('plat_mbl','merk_mbl','nama_mbl','warna_mbl','harga_mbl','status_mbl','kategori_mbl')
    readonly_fields = ['slug']

admin.site.register(mobil, MobilConfig)