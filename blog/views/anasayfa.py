from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q


def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    yazilar = YazilarModel.objects.all().order_by('-guncelleme_tarihi')
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        ).distinct()

    sayf = request.GET.get('sayf')
    paginator = Paginator(yazilar, 2)

    context = {'yazilar': paginator.get_page(sayf)}
    return render(request, 'pages/anasayfa.html', context)
