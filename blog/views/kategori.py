from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator


def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)

    yazilar = kategori.yazi.all().order_by('-guncelleme_tarihi')

    sayf = request.GET.get('sayf')
    paginator = Paginator(yazilar, 2)

    context = {'yazilar': paginator.get_page(sayf)}
    return render(request, 'pages/anasayfa.html', context)
