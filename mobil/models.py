from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class mobil(models.Model):
    #list nanti untuk database Mobil
    kat = (
        ('Matic','Matic'),
        ('Manual','Manual'),
        ('Hybrid','Hybrid')
    )
    status = (
        ('Tersedia','Tersedia'),
        ('Booked','Telah Dibooking')
    )

    plat_mbl        = models.CharField(verbose_name="Nomor Plat Mobil",max_length=50, primary_key=True, unique=True)
    nama_mbl        = models.CharField(verbose_name="Nama Mobil",max_length=225)
    merk_mbl        = models.CharField(verbose_name="Merk",max_length=225)
    foto_mbl        = models.ImageField(verbose_name="Foto Mobil",upload_to='static/mobil/mobil-img', blank=True)
    kategori_mbl    = models.CharField(verbose_name="Kategori",choices=kat ,max_length=225)
    warna_mbl       = models.CharField(verbose_name="Warna Mobil",max_length=225)
    tahun_mbl       = models.IntegerField(verbose_name="Tahun Mobil")
    harga_mbl       = models.IntegerField(verbose_name="Harga Sewa Mobil")
    status_mbl      = models.CharField(verbose_name="Status Mobil",choices=status, max_length=225, default="Tersedia")
    tentang_mbl     = models.TextField(verbose_name="Deskripsi Mobil")
    tgl_db_mbl      = models.DateTimeField(verbose_name="Tanggal Database Dibuat",default=timezone.now)
    slug            = models.SlugField(blank=True , editable=False)
    
    def save(self):
        self.slug = slugify(self.plat_mbl)
        super(mobil, self).save()

    def __str__(self):
        return "{} - {}".format(self.plat_mbl,self.nama_mbl)