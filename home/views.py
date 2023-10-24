from django.shortcuts import render, get_object_or_404
from .models import Article, Post
from django.db.models import Q

def homeView(request):
    articles = Article.objects.all()[:7]
    queryset = Article.objects.order_by('-views')[:10]
    return render(request, template_name='home/home.html', context={'articles': articles, 'popular_articles': queryset})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail/detail.html', {'article': article})

def PopularArticlesListView(request):
    template_name = 'popular_articles.html'
    context_object_name = 'popular_articles'
    queryset = Article.objects.order_by('-views')[:10]
    return render(request, template_name='popular_articles/popular_articles.html', context={'popular_articles': queryset})


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = 'Пожалуйста, введите ключевое слово'
        return render(request, 'home/search.html', {'error_msg': error_msg})


    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'home/search.html', {'error_msg': error_msg, 'post_list': post_list})