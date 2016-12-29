from django.contrib import admin
from .models import Article, News


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'url')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)