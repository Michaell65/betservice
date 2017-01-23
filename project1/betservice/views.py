from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Article, News, Bet
from .forms import BetForm

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


def profile(request):
	bets = Bet.objects.filter(user=request.user).order_by('created')
	return render(request, 'betservice/profile.html', {'bets': bets})


def bet_new(request):
	if request.method == "POST":
		form = BetForm(request.POST)
		if form.is_valid():
			bet = form.save(commit=False)
			bet.user = request.user
			bet.created = timezone.now()
			bet.save()
			return redirect('profile')
	else:
		form = BetForm()
	return render(request, 'betservice/bet_edit.html', {'form': form})
	
	
def bet_delete(request, id):
	Bet.objects.filter(id=id).delete()
	return redirect('profile')
