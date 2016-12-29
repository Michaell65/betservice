from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^articles$', views.article_list, name='article_list'),
    url(r'^articles/([0-9a-z\-]+)$', views.article_detail, name='article_detail'),
    url(r'^news$', views.news_list, name='news_list'),
    url(r'^news/([0-9a-z\-]+)$', views.news_detail, name='news_detail')
]
