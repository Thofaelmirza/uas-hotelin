# Generated by Django 5.0.7 on 2024-07-11 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_hotelin', '0009_remove_produk_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaksi',
            old_name='pesanan',
            new_name='pemesanan',
        ),
    ]
