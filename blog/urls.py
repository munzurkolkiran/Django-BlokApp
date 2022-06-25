from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim/', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yazilarim/', yazilarim, name='yazilarim'),
    path('yazi_ekle/', yazi_ekle, name='yazi_ekle'),
    path('yazi_guncelle/<slug:slug>', yazi_guncelle, name='yazi_guncelle'),
    path('yazi_sil/<slug:slug>', yazi_sil, name='yazi_sil'),

]
