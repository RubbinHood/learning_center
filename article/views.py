from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django import views
from django.core import paginator
from django.template.loader import render_to_string

from . import models


# Create your views here.


class ArticleIndexView(views.View):
    def get(self, request):
        category_id = request.GET.get('category')
        if category_id == 'all':
            category_id = None
        tag_id = request.GET.get('tag')
        if tag_id == 'all':
            tag_id = None
        search = request.GET.get('search')
        categories = models.ArticleCategory.objects.all()
        category = categories.filter(id=category_id).first()
        tag = models.ArticleTag.objects.filter(id=tag_id).first()
        queryset = models.Article.objects.filter(is_active=True)
        if category:
            queryset = queryset.filter(category=category)
        if tag:
            queryset = queryset.filter(tag=tag)
        if search:
            queryset = queryset.filter(
                Q(title__contains=search) | Q(description__contains=search) | Q(text__contains=search))
        paginator_obj = paginator.Paginator(queryset, 6)
        page_obj = paginator_obj.get_page(request.GET.get('page'))
        if queryset:
            return render(request, 'article/article-index.html',
                          {'articles': page_obj, 'categories': categories, 'filtered_category': category,
                           'search': search, 'not_found': False})
        else:
            return render(request, 'article/article-index.html',
                          {'articles': page_obj, 'categories': categories, 'filtered_category': category,
                           'search': search, 'not_found': True})


class ArticleSingleView(views.View):
    def get(self, request, slug):
        article = models.Article.objects.filter(slug=slug, is_active=True).first()
        if article:
            article.views += 1
            article.save()
            return render(request, 'article/article-single.html', {'article': article})
        else:
            raise Http404
