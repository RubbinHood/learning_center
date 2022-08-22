from django.db import models

from user import models as user_models


# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True, blank=True, default=None)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        category = self
        string = [self.title]
        while category.parent:
            string.append(category.parent.title)
            category = category.parent
        string.reverse()
        return '>'.join(string)


class ArticleTag(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='img/article')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=20)
    views = models.IntegerField(default=0)
    tag = models.ManyToManyField(ArticleTag)
    category = models.ForeignKey(ArticleCategory, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
