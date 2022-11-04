from django.contrib.auth.decorators import login_required
from blog.models import YorumModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def yorum_sil(request, id):
    yorum = get_object_or_404(YorumModel, id=id)
    if request.user == yorum.yazan or request.user == yazi.yazar:
        yorum.delete()
        return redirect('detay', slug=yorum.yazi.slug)

    return redirect('anasayfa')
