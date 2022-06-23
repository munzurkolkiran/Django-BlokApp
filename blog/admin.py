from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel
from blog.models import YorumModel


admin.site.register(KategoriModel)


class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'guncelleme_tarihi'
    )


admin.site.register(YazilarModel, YazilarAdmin)


class YorumAdmin(admin.ModelAdmin):
    list_display = (
        'yazan', 'olusturulma_tarihi', 'guncelleme_tarihi'
    )
    search_fields = ('yazan__username', 'icerik')


admin.site.register(YorumModel, YorumAdmin)
