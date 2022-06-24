from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator


def anasayfa(request):
    yazilar = YazilarModel.objects.all().order_by('-guncelleme_tarihi')

    sayf = request.GET.get('sayf')
    paginator = Paginator(yazilar, 2)

    context = {'yazilar': paginator.get_page(sayf)}
    return render(request, 'pages/anasayfa.html', context)
