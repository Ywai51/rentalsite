from django.db import models
from akun.models import NewAkun
from mobil.models import mobil
from motor.models import motor
from django.utils import timezone
import datetime
# Create your models here.

class bookMobil(models.Model):
    status = (
        ('Dipesan','Dipesan'),
        ('Dibayar','Dibayar'),
        ('Dikembalikan','Dikembalikan')
    )
    id_mobil            = models.ForeignKey(mobil,default=1, on_delete=models.CASCADE, unique=False)
    id_penyewa_mbl      = models.ForeignKey(NewAkun,default=1, on_delete=models.CASCADE, unique=False)
    tgl_booking_mbl     = models.DateField(null=True, verbose_name = "Tanggal Mobil Disewa", auto_now=False, editable=True, unique=False)
    waktu_booking_mbl   = models.IntegerField(verbose_name="Lama Sewa Mobil /hari", default=1)
    tgl_kembali_mbl     = models.DateField(null=True, verbose_name = "Tanggal Mobil Kembali", auto_now=False, editable=True, unique=False)
    tgl_reservasi_mbl   = models.DateField(verbose_name="Tanggal Reservasi", default=timezone.now, editable=False)
    no_alternatif_mbl   = models.CharField( verbose_name="No HP Lainnya (opsional)",null=True, blank=True, max_length=25)
    denda_mbl           = models.IntegerField(verbose_name="Denda Sewa Mobil", default=0 , unique=False)
    total_sewa_mbl      = models.IntegerField(verbose_name="Total Harga Sewa Mobil", default=0, unique=False)
    nama_bank_mbl       = models.CharField(verbose_name="Nama Bank yg digunakan", null=True, max_length=150)
    atas_nama_mbl       = models.CharField(verbose_name="Atas Nama Rekening Bank", null=True, max_length=250)
    note_mbl            = models.TextField(verbose_name="Note Pesanan", blank=True, null=True)
    status_sewa_mbl     = models.CharField(verbose_name="Status Sewa Mobil",choices=status, max_length=500, default="Dipesan" ,unique=False)
    
    def set_tanggal(self):
        #Menyamakan tipe TGL
        if self.tgl_kembali_mbl is None:
            self.tgl_kembali_mbl = datetime.datetime.now().date()
        if isinstance(self.tgl_booking_mbl , str):
            self.tgl_booking_mbl = datetime.datetime.strptime(self.tgl_booking_mbl, '%Y-%m-%d').date()
        
        #Kalkulasi denda
        mtrKembali = (self.tgl_kembali_mbl - self.tgl_booking_mbl).days
        mtrKembali = int(mtrKembali)
        denda = self.id_mobil.harga_mbl*25/100

        #GANTI 1 dengan waktu booking untuk booking yang memungkinkan lebih dari 1 hari!
        if mtrKembali <= 1:
            return 0
        else:
            return (mtrKembali - 1) * denda
            
    def save(self, *args, **kwargs):
        #timpa save method
        self.denda_mbl = self.set_tanggal()
        self.total_sewa_mbl += self.denda_mbl
        super(bookMobil, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.id,self.id_mobil,self.id_penyewa_mbl)

class bookMotor(models.Model):
    status = (
        ('Dipesan','Dipesan'),
        ('Dibayar','Dibayar'),
        ('Dikembalikan','Dikembalikan')
    )
    id_motor            = models.ForeignKey(motor,default=1, on_delete=models.CASCADE, unique=False)
    id_penyewa_mtr      = models.ForeignKey(NewAkun,default=1, on_delete=models.CASCADE, unique=False)
    tgl_booking_mtr     = models.DateField(null=True, verbose_name = "Tanggal Motor Disewa", auto_now=False, editable=True, unique=False)
    waktu_booking_mtr   = models.IntegerField(verbose_name="Lama Sewa Motor /hari", default=1)
    
    tgl_kembali_mtr     = models.DateField(null=True, verbose_name = "Tanggal Motor Kembali", auto_now=False, editable=True, unique=False)
    tgl_reservasi_mtr   = models.DateField(verbose_name="Tanggal Reservasi", default=timezone.now, editable=False)
    no_alternatif_mtr   = models.CharField( verbose_name="No HP Lainnya (opsional)",null=True, max_length=25,blank=True)
    denda_mtr           = models.IntegerField(verbose_name="Denda Sewa Motor", default=0 , unique=False)
    total_sewa_mtr      = models.IntegerField(verbose_name="Total Harga Sewa Motor", default=1, unique=False)
    nama_bank_mtr       = models.CharField(verbose_name="Nama Bank yg digunakan", null=True, max_length=150)
    atas_nama_mtr       = models.CharField(verbose_name="Atas Nama Rekening Bank",null=True, max_length=250)
    note_mtr            = models.TextField(verbose_name="Note Pesanan", null=True,blank=True)
    status_sewa_mtr     = models.CharField(verbose_name="Status Sewa Motor",choices=status, max_length=500, default="Dipesan" ,unique=False)
    
    def set_tanggal(self):
        #Menyamakan tipe TGL
        if self.tgl_kembali_mtr is None:
            self.tgl_kembali_mtr = datetime.datetime.now().date()
        if isinstance(self.tgl_booking_mtr , str):
            self.tgl_booking_mtr = datetime.datetime.strptime(self.tgl_booking_mtr, '%Y-%m-%d').date()
        
        #Kalkulasi denda
        mtrKembali = (self.tgl_kembali_mtr - self.tgl_booking_mtr).days
        mtrKembali = int(mtrKembali)
        denda = self.id_motor.harga_mtr*25/100

        #GANTI 1 dengan waktu booking untuk booking yang memungkinkan lebih dari 1 hari!
        if mtrKembali <= 1:
            return 0
        else:
            return (mtrKembali - 1) * denda
            
    def save(self, *args, **kwargs):
        #timpa save method
        self.denda_mtr = self.set_tanggal()
        self.total_sewa_mtr += self.denda_mtr
        super(bookMotor, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.id,self.id_motor,self.id_penyewa_mtr)