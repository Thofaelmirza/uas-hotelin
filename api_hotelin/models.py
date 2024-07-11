from django.db import models
from django.utils import timezone
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
    
class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama
    
class Pemesanan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    kuantitas = models.PositiveIntegerField()
    dipesan_pada = models.DateTimeField(default=timezone.now)
    status_pesanan = models.CharField(max_length=100, default='Menunggu Pembayaran')

    def __str__(self):
        return f"Order {self.id} - {self.produk.nama}"

    def total_harga(self):
        return self.kuantitas * self.produk.harga

    def is_stok_tersedia(self):
        return self.produk.stok >= self.kuantitas
    
class Transaksi(models.Model):
    pesanan = models.ForeignKey(Pemesanan, on_delete=models.CASCADE)
    metode_pembayaran = models.CharField(max_length=100, default='cash')
    tanggal_pembayaran = models.DateTimeField(null=True, blank=True)
    status_pembayaran = models.CharField(max_length=100, default='Belum Dibayar')

    def __str__(self):
        return f"Order {self.id} - {self.produk.nama}"