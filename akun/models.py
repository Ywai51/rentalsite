from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.fields import DateTimeField
from django.utils import timezone


class AkunManager(BaseUserManager):
    def create_superuser(self, email, nama, no_hp, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Belum jadi staff!')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Belum jadi super user!')
        
        return self.create_user(email, nama, no_hp, password, **other_fields)


    def create_user(self, email, nama, no_hp, password, **other_fields):
        if not email:
            raise ValueError('Email dibutuhkan!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nama=nama, no_hp=no_hp, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewAkun(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=254, unique=True)
    nama = models.CharField(verbose_name="nama", max_length=70)
    no_hp = models.CharField(verbose_name="nomor handphone", max_length=15, unique=False)
    tanggal_akun = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AkunManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama','no_hp']

    def __str__(self):
        return self.email