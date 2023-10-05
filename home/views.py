from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article

def homeView(request):
    articles = Article.objects.all()[:7]
    return render(request, template_name='home/home.html', context={'articles': articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail/detail.html', {'article_id': article_id})

class PopularArticlesListView(ListView):
    template_name = 'popular_articles.html'
    context_object_name = 'popular_articles'
    queryset = Article.objects.order_by('-views')[:10]