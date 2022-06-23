from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel
from blog.models import YorumModel
from blog.models import IletisimModel


admin.site.register(KategoriModel)


@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'guncelleme_tarihi'
    )


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = (
        'yazan', 'olusturulma_tarihi', 'guncelleme_tarihi'
    )
    search_fields = ('yazan__username', 'icerik')


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'olusturulma_tarihi'
    )
    search_fields = ('email',)
