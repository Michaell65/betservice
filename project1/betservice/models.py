from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish_date = models.DateField(default=timezone.now())
    description = models.TextField()
    content = RichTextField(null=True)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    publish_date = models.DateField(default=timezone.now())
    description = models.TextField()
    content = RichTextField(null=True)

    def __str__(self):
        return self.title
		
@python_2_unicode_compatible
class Bet(models.Model):
	team1 = models.CharField(max_length=200)
	team2 = models.CharField(max_length=200)
	score1 = models.CharField(max_length=10)
	score2 = models.CharField(max_length=10)
	date = models.DateField(default=timezone.now())
	description = models.TextField()
	user = models.ForeignKey(User, unique=True)
	
	def __str__(self):
		return self.team1 + " vs " + self.team2