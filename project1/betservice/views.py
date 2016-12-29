from django.shortcuts import render, get_object_or_404
from .models import Article, News


def index(request):
    articles = Article.objects.order_by('publish_date').all()[:3]
    news = News.objects.order_by('publish_date').all()[:3]
    return render(request, 'betservice/index.html', {'news': news, 'articles': articles})


def article_list(request):
    articles = Article.objects.order_by('publish_date')
    return render(request, 'betservice/article_list.html', {'articles': articles})


def article_detail(request, url):
    article = get_object_or_404(Article, url=url)
    return render(request, 'betservice/article_detail.html', {'article': article})


def news_list(request):
    news = News.objects.order_by('publish_date')
    return render(request, 'betservice/news_list.html', {'news': news})


def news_detail(request, url):
    news = get_object_or_404(News, url=url)
    return render(request, 'betservice/news_detail.html', {'news': news})


