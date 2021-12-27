from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class motor(models.Model):
    #list nanti untuk database Mobil
    kat = (
        ('Matic','Matic'),
        ('Manual','Manual'),
        ('Kopling','Kopling')
    )
    status = (
        ('Tersedia','Tersedia'),
        ('Booked','Telah Dibooking')
    )

    plat_mtr        = models.CharField(verbose_name="Nomor Plat Motor",max_length=50, primary_key=True, unique=True)
    nama_mtr        = models.CharField(verbose_name="Nama Motor",max_length=225)
    merk_mtr        = models.CharField(verbose_name="Merk",max_length=225)
    foto_mtr        = models.ImageField(verbose_name="Foto Motor",upload_to='static/motor/motor-img', blank=True)
    kategori_mtr    = models.CharField(verbose_name="Kategori",choices=kat ,max_length=225)
    warna_mtr       = models.CharField(verbose_name="Warna Motor",max_length=225)
    tahun_mtr       = models.IntegerField(verbose_name="Tahun Motor")
    harga_mtr       = models.IntegerField(verbose_name="Harga Sewa Motor")
    status_mtr      = models.CharField(verbose_name="Status Motor",choices=status, max_length=225, default="Tersedia")
    tentang_mtr     = models.TextField(verbose_name="Deskripsi Motor")
    tgl_db_mtr  = models.DateTimeField(verbose_name="Tanggal Database Dibuat",default=timezone.now)
    slug            = models.SlugField(blank=True , editable=False)

    def save(self):
        self.slug = slugify(self.plat_mtr)
        super(motor, self).save()

    def __str__(self):
        return "{} - {}".format(self.plat_mtr,self.nama_mtr)