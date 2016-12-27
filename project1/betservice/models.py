from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish_date = models.DateField(default=timezone.now())
    description = models.TextField()

    def __str__(self):
        return self.title