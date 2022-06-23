from django.urls import path, include
from blog.views import iletisim, anasayfa

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('anasayfa/', anasayfa, name='anasayfa'),
    path('iletisim/', iletisim, name='iletisim')
]
