from django.urls import path
from api_hotelin.views import ProdukList, PemesananList, TransaksiList, ProdukDetail, PemesananDetail, TransaksiDetail, UserList, UserDetail

urlpatterns = [
    path('user/',UserList.as_view()),
    path('user/<int:pk>/',UserDetail.as_view()),
    path('produk/',ProdukList.as_view()),
    path('produk/<int:pk>/',ProdukDetail.as_view()),
    path('pemesanan/',PemesananList.as_view()),
    path('pemesanan/<int:pk>/',PemesananDetail.as_view()),
    path('transaksi/',TransaksiList.as_view()),
    path('transaksi/<int:pk>/',TransaksiDetail.as_view()),

]