from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel
from blog.forms import YorumEkleFormModel


def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    print(yazi, '-------------------')
    yorumlar = yazi.yorumlar.all()
    print(request.GET.get('icerik'), '-------------------') 

    if request.method == 'POST':
        yorum_ekle = YorumEkleFormModel(data=request.POST)

        if yorum_ekle.is_valid():
            yorum = yorum_ekle.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()

    yorum_ekle = YorumEkleFormModel()

    context = {'yazi': yazi, 'yorumlar': yorumlar,
               'yorum_ekle': yorum_ekle}
    return render(request, 'pages/detay.html', context)
