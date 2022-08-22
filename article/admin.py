from django.contrib import admin
from django.utils.text import slugify

from . import models


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    def author_full_name(self, article):
        return f'{article.author.first_name} {article.author.last_name}'

    list_display = ['title', 'category', 'author_full_name', 'date']
    list_filter = ['category', 'tag', 'date']
    prepopulated_fields = {'slug': ('title', 'author',)}


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleTag)
admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
