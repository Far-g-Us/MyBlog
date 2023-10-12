from django.shortcuts import render, get_object_or_404
from .models import Article

def homeView(request):
    articles = Article.objects.all()[:7]
    queryset = Article.objects.order_by('-views')[:10]
    return render(request, template_name='home/home.html', context={'articles': articles, 'popular_articles': queryset})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail/detail.html', {'article_id': article_id})

def PopularArticlesListView(request):
    template_name = 'popular_articles.html'
    context_object_name = 'popular_articles'
    queryset = Article.objects.order_by('-views')[:10]
    return render(request, template_name='popular_articles/popular_articles.html', context={'popular_articles': queryset})