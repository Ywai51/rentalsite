# Generated by Django 3.2.8 on 2021-11-27 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor',
            name='foto_mtr',
            field=models.ImageField(blank=True, upload_to='static/motor/motor-img', verbose_name='Foto Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='harga_mtr',
            field=models.IntegerField(verbose_name='Harga Sewa Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='kategori_mtr',
            field=models.CharField(choices=[('Matic', 'Matic'), ('Manual', 'Manual'), ('Kopling', 'Kopling')], max_length=225, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='merk_mtr',
            field=models.CharField(max_length=225, verbose_name='Merk'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='nama_mtr',
            field=models.CharField(max_length=225, verbose_name='Nama Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='plat_mtr',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Nomor Plat Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='status_mtr',
            field=models.CharField(choices=[('Tersedia', 'Tersedia'), ('Booked', 'Telah Dibooking')], default='Tersedia', max_length=225, verbose_name='Status Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='tahun_mtr',
            field=models.IntegerField(verbose_name='Tahun Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='tanggal_db_mtr',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Tanggal Database Dibuat'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='tentang_mtr',
            field=models.TextField(max_length=255, verbose_name='Deskripsi Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='warna_mtr',
            field=models.CharField(max_length=225, verbose_name='Warna Motor'),
        ),
    ]
