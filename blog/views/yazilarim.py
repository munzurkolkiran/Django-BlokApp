from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def yazilarim(request):

    yazilar = request.user.yazilar.order_by('-guncelleme_tarihi')

    sayf = request.GET.get('sayf')
    paginator = Paginator(yazilar, 2)

    context = {'yazilar': paginator.get_page(sayf)}
    return render(request, 'pages/yazilarim.html', context)
