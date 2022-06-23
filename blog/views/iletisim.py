from django.shortcuts import render
from django.http import HttpResponse


def iletisim(request):

    return render(request, 'pages/iletisim.html')
