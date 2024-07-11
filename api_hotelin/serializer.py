from rest_framework import serializers
from .models import Produk, Pemesanan, Transaksi
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    Produk = serializers.PrimaryKeyRelatedField(many=True, queryset=Produk.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'Produk']

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class PemesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'