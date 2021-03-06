from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^articles$', views.article_list, name='article_list'),
    url(r'^articles/([0-9a-z\-]+)$', views.article_detail, name='article_detail'),
    url(r'^news$', views.news_list, name='news_list'),
    url(r'^news/([0-9a-z\-]+)$', views.news_detail, name='news_detail'),
	url(r'^accounts/profile/$', views.profile, name='profile'),
	url(r'^bet/new/$', views.bet_new, name='bet_new'),
	url(r'^bet/delete/([0-9]+)$', views.bet_delete, name='bet_delete'),
	url(r'^bet/byuser/([0-9]+)$', views.bet_list_by_user, name='bet_list_by_user'),
	url(r'^bet/list$', views.bet_list, name='bet_list'),
]
