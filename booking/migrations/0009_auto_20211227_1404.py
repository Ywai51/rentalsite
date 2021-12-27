# Generated by Django 3.2.8 on 2021-12-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_bookmotor_tgl_kembali_mtr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmobil',
            name='no_alternatif_mbl',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='No HP Lainnya (opsional)'),
        ),
        migrations.AlterField(
            model_name='bookmobil',
            name='note_mbl',
            field=models.TextField(blank=True, null=True, verbose_name='Note Pesanan'),
        ),
        migrations.AlterField(
            model_name='bookmotor',
            name='no_alternatif_mtr',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='No HP Lainnya (opsional)'),
        ),
        migrations.AlterField(
            model_name='bookmotor',
            name='note_mtr',
            field=models.TextField(blank=True, null=True, verbose_name='Note Pesanan'),
        ),
    ]
