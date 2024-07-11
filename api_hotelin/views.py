from rest_framework import generics
from api_hotelin.serializer import ProdukSerializer, PemesananSerializer, TransaksiSerializer, UserSerializer
from api_hotelin.models import Produk, Pemesanan, Transaksi
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework import permissions
from api_hotelin.permissions import IsOwnerOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProdukList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PemesananList(generics.ListCreateAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSerializer

class PemesananDetail(APIView):
    def get_object(self, pk):
        try:
            return Pemesanan.objects.get(pk=pk)
        except Pemesanan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(pemesanan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(pemesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pemesanan = self.get_object(pk)
        pemesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransaksiList(generics.ListCreateAPIView):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer

class TransaksiDetail(APIView):
    def get_object(self, pk):
        try:
            return Transaksi.objects.get(pk=pk)
        except Transaksi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transaksi = self.get_object(pk)
        serializer = TransaksiSerializer(transaksi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transaksi = self.get_object(pk)
        serializer = TransaksiSerializer(transaksi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transaksi = self.get_object(pk)
        transaksi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)