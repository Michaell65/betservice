from django.contrib import admin
from .models import Article, News, Bet


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'url')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

	
class BetAdmin(admin.ModelAdmin):
    list_display = ('date', 'team1', 'score1', 'team2', 'score2')

admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Bet, BetAdmin)
