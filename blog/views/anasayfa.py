from django.shortcuts import render


def anasayfa(request):
    context = {
        'isim': 'munzur kolkiran'
    }
    return render(request, 'pages/anasayfa.html', context)
