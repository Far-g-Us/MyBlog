from django.shortcuts import render, get_object_or_404
from .models import Arta

def homeView(request):
    articles = Arta.objects.all()
    return render(request, template_name='home/home.html', context={'articles': articles})

def detail(request,article_id):
    article = get_object_or_404(Arta, pk=article_id)
    return render(request, 'detail/detail.html', {'article_id': article_id})