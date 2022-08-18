from django.db import models

from user import models as user_models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='img/article')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=20)
    views = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)